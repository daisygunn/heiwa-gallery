from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibitions, name='exhibitions'),
]