from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'population', 'region', 'subregion', 'alpha2Code', 'alpha3Code', 'additional_info')
