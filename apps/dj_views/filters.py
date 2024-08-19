import django_filters as filter

from .models import *

class StateFilter(filter.FilterSet):
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')
    population = filter.NumberFilter(field_name='population', lookup_expr='gt')

    class Meta:
        model = State
        fields = ['name', 'population']