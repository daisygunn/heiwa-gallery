from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """ allows admin to view user profiles """
    model = UserProfile
    readonly_fields = ('user', 'registration_date',)
    fields = ('full_name', 'email', 'phone_number', 
              'flat_house', 'street_address', 'town_city', 'county',
              'country', 'postcode',)
  
    list_display = ('full_name', 'email',)
    # displays most recent orders on the top
    ordering = ('-registration_date',)
