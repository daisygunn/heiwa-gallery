from django.urls import path
from . import views

urlpatterns = [
     path('', views.UserProfiles.as_view(), name="user_profile"),
]
