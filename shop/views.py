from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterForm




def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    order, created = Order.objects.get_or_create(user=user)  
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
    order_item.save()

    # Add the order_item to the order's items
    order.items.add(order_item)  # Make sure this line is there to associate OrderItem with Order

    return redirect('cart')

@login_required  
def cart(request):
    user = request.user  
    try:
        order = Order.objects.get(user=user)  
        total_price = sum(item.product.price * item.quantity for item in order.items.all())
    except Order.DoesNotExist:
        order = None
        total_price = 0
    print(order.items.all()) 

    return render(request, 'shop/cart.html', {'order': order, 'total_price': total_price})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')  # Replace 'home' with your landing page
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})