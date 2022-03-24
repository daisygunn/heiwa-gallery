import uuid

from django.db import models
from django.db.models import Sum
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
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')
    order_sucess = models.BooleanField(default=False)

    def _generate_order_number(self):
        """ generate a random, unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Updates total cost each time an order item is added """
        self.order_total = self.orderitems.aggregate(
            Sum('orderitem_total'))['orderitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """ if the order doesn't have an order number, create one """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """ individual items in order """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item total
        and update the order total.
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} in {self.product.size} on order {self.order.order_number}'