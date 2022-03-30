from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ form for users to place order """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                  'flat_house', 'street_address', 'town_city', 
                  'county', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email',
            'phone_number': 'Phone number',
            'flat_house': 'Flat/House number',
            'street_address': 'Street Address',
            'town_city': 'Town or City',
            'county': 'County',
            'postcode': 'Post code',
            'country': 'Country (delivery only possible in UK)',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'w-100 p-1 mb-2'