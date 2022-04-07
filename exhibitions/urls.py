from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibitions_list, name='exhibitions_list'),
    path('add_exhibition/', views.AddExhibition.as_view(),
         name='add_exhibition'),
]
