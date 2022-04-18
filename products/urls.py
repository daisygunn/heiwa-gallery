from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProducts.as_view(), name='all_products'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('product_management/', views.ProductManagement.as_view(),
         name='product_management'),
    path('edit_product/<pk>', views.EditProduct.as_view(),
         name='edit_product'),
    path('delete_product/<pk>', views.DeleteProduct.as_view(),
         name='delete_product'),
    path('stock/<pk>', views.StockManagement.as_view(), name='stock'),
]
