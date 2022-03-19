from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasketOverview.as_view(), name="basket_overview"),
    path('add_to_basket/<pk>', views.add_product_to_basket, name='add_product_to_basket'),
]