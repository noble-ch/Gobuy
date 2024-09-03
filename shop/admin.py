from django.contrib import admin
from .models import Product, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # Show these fields in the list view
    search_fields = ('name',)  # Add a search box for the name field

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'date_ordered')
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('date_ordered',)  # Filter by order date

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')

# Register your models with customized admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
