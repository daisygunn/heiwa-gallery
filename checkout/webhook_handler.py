from django.http import HttpResponse
from products.models import Product
from .models import Order, OrderItem
from user_account.models import UserProfile

import json
import time


class StripeWhHandler:
    """ handle all stripe webhooks """
    def __init__(self, request):
        """ init method """
        self.request = request

    def handle_event(self, event):
        """ handle all generic events """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ handle all successful events """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_address = intent.metadata.save_address
        # get details from payment intent
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        # Update profile information if save_address was checked
        user_profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = UserProfile.objects.get(user__username=username)
            if save_address == "true":
                user_profile.default_phone_number = (
                    shipping_details.phone)
                user_profile.default_flat_house = (
                    shipping_details.address.line1)
                user_profile.default_street_address = (
                    shipping_details.address.line2)
                user_profile.default_town_city = (
                    shipping_details.address.city)
                user_profile.default_county = (
                    shipping_details.address.state)
                user_profile.default_country = (
                    shipping_details.address.country)
                user_profile.default_postcode = (
                    shipping_details.address.postal_code)
                user_profile.save()
        order_exists = False
        # prevent the order being added twice
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    flat_house__iexact=shipping_details.address.line1,
                    street_address__iexact=shipping_details.address.line2,
                    town_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    order_total=order_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            # if the order does not exist then add 1 attempt
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # if it does exist then do not add again
        if order_exists:
            return HttpResponse(
                content=f'Webhook received:\
                {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # create order if attempts are more than 5
            order = None
            try:
                for pk, quantity in json.loads(basket).items():
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        flat_house=shipping_details.address.line1,
                        street_address=shipping_details.address.line2,
                        town_city=shipping_details.address.city,
                        county=shipping_details.address.state,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    product = Product.objects.get(pk=pk)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    stock = product.get_stock_level()
                    product.quantity_in_stock = stock - quantity
                    product.save()
                    order_item.save()
                    order.order_success = True
            except Exception as error:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"webhook received: {event['type']} |\
                    Fail: error: {error}",
                    status=500)
            return HttpResponse(
                content=f"webhook received: {event['type']} |\
                    SUCCESS: Order created by webhook",
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ handle all unsuccessful events """
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)
