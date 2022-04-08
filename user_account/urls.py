from django.urls import path
from . import views

urlpatterns = [
     path('', views.account_overview, name="account_overview"),
     path('user_profile/', views.user_profile_display, name="user_profile"),
     path('user_orders/', views.user_orders, name="user_orders"),
     path('add_to_wishlist/<pk>', views.add_to_wishlist, name="add_to_wishlist"),
     path('wishlist/', views.user_wishlist, name="wishlist"),
]
