from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibitions_list, name='exhibitions_list'),
]