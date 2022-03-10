from django import forms
from .models import Product, Category


class AddProductForm(forms.ModelForm):
    """ form to add a new product to the DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'style', 'photographer_artist', 'size', 
                  'quantity_in_stock', 'price', 'image')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-100'