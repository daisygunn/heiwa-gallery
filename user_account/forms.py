from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ form for users to place order """
    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'phone_number',
                  'default_flat_house', 'default_street_address',
                  'default_town_city', 'default_county',
                  'default_postcode', 'default_country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'default_flat_house': 'Flat/House number',
            'default_street_address': 'Street Address',
            'default_town_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Post code',
            'default_country': 'Country',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'w-100 p-1 mb-2'
