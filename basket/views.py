from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from django.views import View


class BasketOverview(View):
    """ Returns basket page where overview 
    of customer basket is displayed """
    def get(self, request):
        """ get request """
       
        return render(request, 'basket/basket.html')


def add_product_to_basket(request, pk):
    """ add product to bag """
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})
    if product.in_stock:
        if pk in list(basket.keys()):
            basket[pk] += quantity
        else:
            basket[pk] = quantity
        messages.success(request, f"{product} has been added to your basket.")
    else:
        messages.error(
            request, f"{product} is not in stock and" 
            " therefore cannot be added.")
    
    request.session['basket'] = basket
    # import pdb; pdb.set_trace()
    print(request.session['basket'])
    return redirect(redirect_url)