from django.db import models
from django.db.models import JSONField

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subregion(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.region.name})"

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.IntegerField()
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)
    alpha2Code = models.CharField(max_length=3, null=True, blank=True)
    alpha3Code = models.CharField(max_length=3, null=True, blank=True)
    additional_info = models.JSONField(null=True, blank=True)  # Define um dicionário vazio como valor padrão  

    def __str__(self):
        return self.name
