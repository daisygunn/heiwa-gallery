from django.urls import path
from . import views

urlpatterns = [
    path('', views.exhibitions_list, name='exhibitions_list'),
    path('exhibition_management/', views.exhibition_management,
         name='exhibition_management'),
    path('add_exhibition/', views.AddExhibition.as_view(),
         name='add_exhibition'),
    path('edit_exhibition/<pk>', views.EditExhibition.as_view(),
         name='edit_exhibition'),
    path('delete_exhibition/<pk>', views.DeleteExhibition.as_view(),
         name='delete_exhibition'),
]
