from django.urls import path
from . import views

urlpatterns = [
     path('', views.user_profile_display, name="user_profile"),
     path('user_orders/', views.user_orders, name="user_orders"),
]
