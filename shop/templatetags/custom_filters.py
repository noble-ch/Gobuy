from django import template

register = template.Library()

@register.filter
def total_sum(order_items):
    return sum(item.product.price * item.quantity for item in order_items)
