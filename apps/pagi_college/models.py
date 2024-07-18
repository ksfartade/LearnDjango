from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department, null=True, blank=True)