from django.db import models

# Create your models here.

class Department1(models.Model):
    name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    departments = models.ManyToManyField(Department1, null=True, blank=True)