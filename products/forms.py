from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ form to add a new product to the DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'style', 'photographer_artist', 'size', 
                  'quantity_in_stock', 'price', 'image')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'product name',
            'style': 'style',
            'photographer_artist': 'photographer/artist',
            'size': 'size',
            'quantity_in_stock': 'quantity in stock',
            'price': 'price',
            'image': 'product image',
        }
        
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'w-100 mb-2'


class EditProductForm(forms.ModelForm):
    """ form to edit product in DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'style', 'photographer_artist', 'size', 
                  'quantity_in_stock', 'price', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'product name',
            'style': 'style',
            'photographer_artist': 'photographer/artist',
            'size': 'size',
            'quantity_in_stock': 'quantity in stock',
            'price': 'price',
            'image': 'product image',
        }
        
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields['quantity_in_stock'].widget.attrs['readonly'] = True
            self.fields['quantity_in_stock'].widget.attrs['class'] = 'hidden'
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'w-100 mb-2'


class StockForm(forms.ModelForm):
    """ form to add a new product to the DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'quantity_in_stock',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            labels = {
                'name': 'Product name',
                'quantity_in_stock': 'Updated quantity in stock',
            }
            self.fields[field].label = labels[field]
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields[field].widget.attrs['class'] = 'w-100 mb-2'
