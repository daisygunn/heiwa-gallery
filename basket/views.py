from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from products.models import Product


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
        stock = product.get_stock_level()
        if quantity > 0 and stock >= quantity:
            if pk in list(basket.keys()):
                if basket[pk] + quantity > stock:
                    messages.error(request, "Sorry, we do not have enough in "
                                            f"stock of {product}.")
                else:
                    basket[pk] += quantity
                    messages.success(
                        request, f"{product} has been updated in your basket.")
            else:
                basket[pk] = quantity
                messages.success(
                    request, f"{product} has been added to your basket.")
        elif quantity > 0 and stock < quantity:
            messages.error(request, "Sorry, we do not have enough in "
                                    f"stock of {product}.")
    else:
        messages.error(
                request, f"{product} is not in stock and"
                " therefore cannot be added.")

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def change_quantity(request, pk):
    """ add product to bag """
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    stock = product.get_stock_level()
    if product.in_stock:
        if pk in list(basket.keys()):
            if quantity > 0 and stock >= quantity:
                basket[pk] = quantity
                messages.success(
                    request, f"{product} has been updated in your basket.")
            elif quantity > 0 and stock < quantity:
                messages.error(
                    request, f"Sorry, we only have {stock} in stock of"
                             f" {product} please reduce the number in"
                             " your basket.")
            else:
                basket.pop(pk)
                messages.success(
                    request, f"{product} has been removed from your basket.")
        else:
            messages.error(request, f"{product} is not in your basket.")
    else:
        messages.error(
            request, f"{product} is not in stock and"
            " therefore cannot be added.")

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_product(request, pk):
    """ add product to bag """
    product = get_object_or_404(Product, pk=pk)
    basket = request.session.get('basket', {})

    if pk in list(basket.keys()):
        basket.pop(pk)
        messages.success(request, f"{product} has been removed basket.")
    else:
        messages.error(request, f"{product} is not in your basket.")

    request.session['basket'] = basket
    return redirect('basket_overview')
