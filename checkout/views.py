from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

import stripe
import json

from basket.context_processors import basket_contents
from products.models import Product
from user_account.models import UserProfile
from user_account.forms import UserProfileForm
from .forms import OrderForm
from .models import Order, OrderItem


@require_POST
def cache_checkout_data(request):
    """ to store save address info """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # update the payment intents metadata, passing the information across
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_address': request.POST.get('save_address'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, "Something isn't quite right.")
        return HttpResponse(content=error, status=400)


@require_POST
def send_confirmation_email(request, order_number):
    """ Function to send email after order saved """
    order = Order.objects.get(order_number=order_number)
    customer_name = order.full_name
    # email_from = settings.EMAIL_HOST_USER
    email_from = "orders@heiwa.com"
    address = order.full_address()
    subject = f"Order confirmation from Heiwa - order\
             number {order.order_number}"
    message = (f"Thank you for your order {customer_name}.\n"
               f"Order number - {order.order_number}\n"
               f"Order total - {order.order_total}\n"
               f"Delivery address - {address}.")

    recipient_list = (order.email,)
    send_mail(
        subject, message, email_from, recipient_list, fail_silently=False)


def checkout(request):
    """ checkout """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # post method
    if request.method == 'POST':
        # get the basket or render an empty basket if it doesn't exist
        basket = request.session.get('basket', {})
        # get the form data from post request
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'flat_house': request.POST.get('flat_house'),
            'town_city': request.POST.get('town_city'),
            'street_address': request.POST.get('street_address'),
            'county': request.POST.get('county'),
            'postcode': request.POST.get('postcode'),
            'country': request.POST.get('country'),
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.stripe_pid = request.POST.get(
                'client_secret').split('_secret')[0]
            # save the basket in the order model
            order.original_basket = json.dumps(basket)
            order.save()
            # for each item & quantity
            for pk, quantity in basket.items():
                try:
                    product = Product.objects.get(pk=pk)
                    # create an order item
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    # get the stock level, check the quantity desired
                    # is not more than the stock
                    stock = product.get_stock_level()
                    print(stock)
                    if stock >= quantity:
                        # change the stock level
                        product.quantity_in_stock = stock - quantity
                        print(product.quantity_in_stock)
                        # update the stock label
                        product.change_stock_label()
                        product.save()
                        order_item.save()
                    else:
                        # if we do not have enough in stock
                        messages.error(
                            request, "We do not have enough of "
                                     f"{product.name} in stock for you"
                                     " to purchase your desired amount."
                                     " Please review your basket.")
                        order.delete()
                        return redirect(reverse('basket_overview'))
                except Product.DoesNotExist:
                    messages.error(
                        request, "Unfortunately one of"
                        " the items in your basket is not currently"
                        " being sold.")
                    order.delete()
                    return redirect(reverse('basket_overview'))
            # update order_success label
            order.order_success = True
            order_number = order.order_number
            # send confirmation email to customer
            send_confirmation_email(request, order_number)
            request.session['save_address'] = 'save-address' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "something wrong with form")
            return render(request, 'checkout/checkout.html',
                          {'form': order_form, })
    else:
        if request.user.is_authenticated:
            # get user profile
            user = UserProfile.objects.get(user=request.user)
            # pre-populate for the form with data saved against profile
            form_data = {
                'full_name': user.full_name,
                'email': user.email,
                'phone_number': user.phone_number,
                'flat_house': user.default_flat_house,
                'town_city': user.default_town_city,
                'street_address': user.default_street_address,
                'county': user.default_county,
                'postcode': user.default_postcode,
                'country': user.default_country,
            }
            order_form = OrderForm(form_data)
        else:
            order_form = OrderForm()
        # get basket
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There isn't currently anything"
                           " in your basket.")
            return(redirect('all_products'))
        # define payment parameters
        current_basket = basket_contents(request)
        payment_due = current_basket['total_cost']
        stripe_payment_amount = round(payment_due * 100)
        stripe.api_key = stripe_secret_key
        # create stripe intent
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
                       'client_secret': intent.client_secret, })


def checkout_success(request, order_number):
    """ handle success """
    save_address = request.session.get('save_address')
    print(save_address)
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = user
        order.save()
        # Save the user's default billing details
        if save_address:
            print('saving')
            default_data = {
                'full_name': user.full_name,
                'email': user.email,
                'phone_number': user.phone_number,
                'default_flat_house': order.flat_house,
                'default_town_city': order.town_city,
                'default_street_address': order.street_address,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(
                data=default_data, instance=user)
            if user_profile_form.is_valid():
                # profile being updated
                user_profile_form.save()

    messages.success(request, "Order processed - your order number is"
                     f'{order_number}.')

    if 'basket' in request.session:
        del request.session['basket']

    return render(request, 'checkout/checkout_success.html',
                  {'order': order, })
