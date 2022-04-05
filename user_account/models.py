from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ UserProfile model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=False, blank=False)
    default_flat_house = models.CharField(
        max_length=80, null=False, blank=False)
    default_town_city = models.CharField(
        max_length=40, null=False, blank=False)
    default_street_address = models.CharField(
        max_length=80, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)
    registration_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user