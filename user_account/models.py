from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class UserWishlist(models.Model):
    """ wishlist model """
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="user_wishlist",
        null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_wishlist",
        null=False, blank=False)

    def __str__(self):
        return self.product.name
