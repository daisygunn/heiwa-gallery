from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasketOverview.as_view(), name="basket_overview"),
    path('add_to_bag/<pk>', views.add_product_to_bag, name='add_product_to_bag'),
]