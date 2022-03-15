from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='all_products'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('update_products/', views.UpdateProduct.as_view(), name='update_products'),
    path('stock/', views.StockManagement.as_view(), name='stock'),
]