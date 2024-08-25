from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'capital', 'population', 'region', 'subregion', 'alpha2Code', 'alpha3Code', 'additional_info']
    
    def clean(self):
        cleaned_data = super().clean()
        additional_info = cleaned_data.get('additional_info')
        if additional_info is None:
            cleaned_data['additional_info'] = {}
        return cleaned_data