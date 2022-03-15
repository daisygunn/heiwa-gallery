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

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-100'


class EditProductForm(forms.ModelForm):
    """ form to edit product in DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'style', 'photographer_artist', 'size', 
                  'quantity_in_stock', 'price', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity_in_stock'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-100'


class StockForm(forms.ModelForm):
    """ form to add a new product to the DB """
    class Meta:
        """ product form """
        model = Product
        fields = ('name', 'quantity_in_stock',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-100'    
