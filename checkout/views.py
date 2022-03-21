from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.conf import settings
from basket.context_processors import basket_contents
from .forms import OrderForm

import stripe 


class Checkout(View):
    """ checkout view """
    def get(self, request):
        """ get request """
        order_form = OrderForm()
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

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
        print(intent)
        return render(request, 'checkout/checkout.html',
                      {'form': order_form,
                       'stripe_public_key': stripe_public_key,
                       'client_secret': intent.client_secret,})
