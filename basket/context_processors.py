

def basket_contents(request):
    """ basket context """

    items_in_basket = []
    total = 0
    count = 0

    context = {
        'items_in_basket': items_in_basket,
        'total_cost': total,
        'product_count': count,
    }

    return context
