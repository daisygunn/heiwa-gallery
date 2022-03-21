from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ form for users to place order """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                  'flat_house', 'town_city', 'street_address', 
                  'county', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'flat_house': 'Flat/House number',
            'town_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County',
            'postcode': 'Post code',
            'country': 'Country (delivery only possible in UK)',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'w-100 mb-2'