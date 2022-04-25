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
    # If there is no post data then the user has tried
    # to override url
    if request.POST.get(
        'quantity') is None and request.POST.get(
            'redirect_url') is None:
        messages.warning(
                request, "You have tried to add a product without "
                "a quantity which is not allowed.")
        # redirect back to all products
        return redirect('all_products')
    else:
        # get quantity and redirect url from POST data
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
    # get basket instance or create basket if it doesn't exist
    basket = request.session.get('basket', {})
    if product.in_stock:
        # get the stock level for the product
        stock = product.get_stock_level()
        # If quantity added is bigger than 0 and the stock level
        # is bigger than the quantity being added
        if quantity > 0 and stock >= quantity:
            # if product is already in basket
            if pk in list(basket.keys()):
                # if the quantity in the basket + quantity being added
                # is bigger than the stock level
                if basket[pk] + quantity > stock:
                    # do not add to basket
                    messages.error(request, "Sorry, we do not have enough in "
                                            f"stock of {product}.")
                else:
                    # if there is enough in stock, add to basket
                    basket[pk] += quantity
                    messages.success(
                        request, f"{product} has been updated in your basket.")
            else:
                # if product isn't in basket already, then add it
                basket[pk] = quantity
                messages.success(
                    request, f"{product} has been added to your basket.")
        # if there is less stock than the quantity being added then do not add
        elif quantity > 0 and stock < quantity:
            messages.error(request, "Sorry, we do not have enough in "
                                    f"stock of {product}.")
    else:
        messages.error(
                request, f"{product} is not in stock and"
                " therefore cannot be added.")
    # update the sessions's basket
    request.session['basket'] = basket
    # redirect back to same page
    return redirect(redirect_url)


def change_quantity(request, pk):
    """ add product to bag """
    product = get_object_or_404(Product, pk=pk)
    # get quantity and redirect url from POST data
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get basket instance or create basket if it doesn't exist
    basket = request.session.get('basket', {})
    # get stock level for product
    stock = product.get_stock_level()
    # if in stock
    if product.in_stock:
        if pk in list(basket.keys()):
            # If quantity added is bigger than 0 and the stock level
            # is bigger than the quantity being added
            if quantity > 0 and stock >= quantity:
                # update the quantity
                basket[pk] = quantity
                messages.success(
                    request, f"{product} has been updated in your basket.")
            elif quantity > 0 and stock < quantity:
                # if the quantity being added is bigger than the stock level
                # do not update the basket
                messages.error(
                    request, f"Sorry, we only have {stock} in stock of"
                              f" {product} please reduce the number in"
                              " your basket.")
            else:
                # if quantity is 0 then remove from basket
                basket.pop(pk)
                messages.success(
                    request, f"{product} has been removed from your basket.")
        else:
            # if product is not in the basket
            messages.error(request, f"{product} is not in your basket.")
    else:
        # if product is not in stock
        messages.error(
            request, f"{product} is not in stock and"
            " therefore cannot be added.")
    # update the basket
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_product(request, pk):
    """ add product to bag """
    product = get_object_or_404(Product, pk=pk)
    # get basket instance or create basket if it doesn't exist
    basket = request.session.get('basket', {})
    # if product is in basket
    if pk in list(basket.keys()):
        # remove from basket
        basket.pop(pk)
        messages.success(request, f"{product} has been removed basket.")
    else:
        # if product is not in the basket
        messages.error(request, f"{product} is not in your basket.")
    # update the basket
    request.session['basket'] = basket
    return redirect('basket_overview')
