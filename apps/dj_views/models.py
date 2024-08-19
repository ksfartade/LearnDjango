from django.db import models

# Create your models here.

class Country(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    population  = models.IntegerField(null=True)

class State(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    population  = models.IntegerField(null=True)
    country     = models.ForeignKey(Country, related_name='states', null=True, on_delete=models.SET_NULL)
