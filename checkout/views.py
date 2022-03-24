from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages
from django.conf import settings

import stripe 

from basket.context_processors import basket_contents
from .forms import OrderForm
from products.models import Product
from .models import Order, OrderItem


def checkout(request):
    """ checkout """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        print('post working')
        basket = request.session.get('basket', {})
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'flat_house': request.POST.get('flat_house'),
            'town_city': request.POST.get('town_city'),
            'street_address': request.POST.get('town_city'),
            'county': request.POST.get('county'),
            'postcode': request.POST.get('postcode'),
            'country': request.POST.get('country'),
        }
        order_form = OrderForm(data=request.POST)
       
        if order_form.is_valid():
            order = order_form.save()
            for pk, quantity in basket.items():
                try:
                    product = Product.objects.get(pk=pk)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, "Unfortunately one of"
                        " the items in your basket is not currently"
                        " being sold.")
                    order.delete()
                    return redirect(reverse('basket_overview'))            
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "something wrong with form")
            return render(request, 'checkout/checkout.html',
                      {'form': order_form, })
    else:
        order_form = OrderForm()
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There isn't currently anything"
                           " in your basket.")
            return(redirect('all_products'))
        
        current_basket = basket_contents(request)
        payment_due = current_basket['total_cost']
        stripe_payment_amount = round(payment_due * 100)
        stripe.api_key = stripe_secret_key
        
        intent = stripe.PaymentIntent.create(
            amount=stripe_payment_amount,
            currency='gbp',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return render(request, 'checkout/checkout.html',
                      {'form': order_form,
                       'stripe_public_key': stripe_public_key,
                       'client_secret': intent.client_secret,
                     })


def checkout_success(request, order_number):
    """ handle success """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, "Order processed - your order number is"
                     f'{order_number}.')

    if 'basket' in request.session:
        del request.session['basket']
    
    return render(request, 'checkout/checkout_success.html',
                 {'order': order,})