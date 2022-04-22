from django import template


register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    # Calculate subtotal filter to be used across site
    return price * quantity
