import django_filters
from .views import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    release_before = django_filters.NumberFilter(field_name='year', lookup_expr='lt')
    release_after = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year = django_filters.NumberFilter()
