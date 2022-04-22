from django import forms
from django.conf import settings
from .models import Exhibitions


class ExhibitionForm(forms.ModelForm):
    """ Exhibitions form """
    date_starting = forms.DateField(input_formats=settings.DATE_INPUT_FORMAT)
    date_finishing = forms.DateField(input_formats=settings.DATE_INPUT_FORMAT)

    class Meta:
        """ Exhibitions form """
        model = Exhibitions
        fields = ('name', 'style', 'description', 'photographer_artist',
                  'entrance_fee', 'gallery_area', 'date_starting',
                  'date_finishing', 'display',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'exhibition name',
            'style': 'style',
            'description': 'exhibition description',
            'photographer_artist': 'photographer/artist',
            'entrance_fee': 'entrance fee',
            'gallery_area': 'gallery area exhibition will use',
            'date_starting': 'start date',
            'date_finishing': 'end date',
            'display': 'show exhibition',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields['display'].label = placeholder
            self.fields[field].widget.attrs['class'] = 'w-100 p-2 mb-2'
            # make date fields datepickers
            self.fields['date_starting'].widget.attrs['class'] = (
                'date-picker dateinput w-100 p-2 mb-2')
            self.fields['date_finishing'].widget.attrs['class'] = (
                'date-picker dateinput w-100 p-2 mb-2')
