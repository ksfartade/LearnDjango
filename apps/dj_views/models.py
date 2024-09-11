from typing import Iterable
from django.db import models

# Create your models here.

class Country(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    population  = models.IntegerField(null=True, blank=True)
    

class State(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    population  = models.IntegerField(null=True)
    country     = models.ForeignKey(Country, related_name='states', null=True, on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    # form_date   = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name
    
