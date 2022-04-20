from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """ allows admin to add/edit order items in the admin panel """
    model = OrderItem
    readonly_fields = ('orderitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order model admin """
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'order_total',
                       'stripe_pid', 'original_basket',)

    fields = ('order_number', 'full_name', 'email', 'phone_number', 
              'flat_house', 'street_address', 'town_city', 'county',
              'country', 'postcode', 'order_date', 'order_total', 'stripe_pid',
              'original_basket',)
  
    list_display = ('order_number', 'order_date', 'full_name',
                    'order_total', 'original_basket',)
    # displays most recent orders on the top
    ordering = ('-order_date',)
