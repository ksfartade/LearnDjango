from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.views import APIView

from .serializers import *
from .views import *


class StateList(ListAPIView):
    pagination_class = None
    serializer_class = StateSerializer
    queryset = State.objects.all()
    lookup_field = ['country__name']

    # def get_queryset(self):
    #     queryset = State.objects.filter(country__name='india')
    #     return queryset

    # def list(request, *args, **kwargs):
    #     return Response("Overried the list method of ListAPIView", status=200)


class StateSingle(generics.RetrieveAPIView):
    pagination_class = None
    serializer_class = StateSerializer
    queryset = State.objects.all()
    lookup_field = 'name'


class StateGenericAPIView(GenericAPIView):
    pagination_class = None
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get(self, request, **kwargs):
        return Response("Hey in get method of genericAPIView", status=200)
    
    def patch(self, request, **kwargs):
        return Response("in the patch method of generics API View", status=200)
