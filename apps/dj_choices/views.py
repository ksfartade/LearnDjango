from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import SY, Department
from .serializer import SYSerializer, DepSerializer

class SYViewSet(viewsets.ModelViewSet):
    queryset = SY.objects.all()
    serializer_class = SYSerializer

class DepViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepSerializer