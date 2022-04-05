from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """ allows admin to view user profiles """
    model = UserProfile
    readonly_fields = ('user', 'registration_date',)
    fields = ('user', 'full_name', 'email', 'phone_number',
              'default_flat_house', 'default_street_address',
              'default_town_city', 'default_county',
              'default_postcode', 'default_country')
  
    list_display = ('full_name', 'email',)
    ordering = ('-registration_date',)
