from django.db import models
from products.models import Product

country_choices = (
    ('United Kingdom', 'United Kingdom'),
)


class Order(models.Model):
    """ order model """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    flat_house = models.CharField(max_length=80, null=False, blank=False)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(
        choices=country_choices, default="United Kingdom", null=False,
        blank=False, max_length=20)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    order_sucess = models.BooleanField()


class OrderItem(models.Model):
    """ individual items in order """
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='orderitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)
