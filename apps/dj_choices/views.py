from django.shortcuts import render
from rest_framework import viewsets
from .models import SY
from .serializer import SYSerializer

class SYViewSet(viewsets.ModelViewSet):
    queryset = SY.objects.all()
    serializer_class = SYSerializer
