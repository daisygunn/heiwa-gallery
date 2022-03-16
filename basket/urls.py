from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasketOverview.as_view(), name="basket_overview"),
]