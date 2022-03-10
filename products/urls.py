from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='all_products'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('stock/', views.StockManagement.as_view(), name='stock'),
]