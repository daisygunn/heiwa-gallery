from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='all_products'),
]