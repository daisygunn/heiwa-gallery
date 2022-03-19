from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """ basket context """

    items_in_basket = []
    total = 0
    count = 0
    basket = request.session.get('basket', {})

    for pk, quantity in basket.items():
        product = get_object_or_404(Product, pk=pk)
        total += quantity * product.price
        count += quantity
        items_in_basket.append({
            'pk': pk,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'items_in_basket': items_in_basket,
        'total_cost': total,
        'product_count': count,
        'basket': basket,
        'product': product,
    }

    return context
