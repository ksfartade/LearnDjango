from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework import mixins, viewsets

from .serializers import *
from .views import *
from .filters import *
import django_filters


class StateList(ListAPIView):
    pagination_class = None
    serializer_class = StateSerializer
    queryset = State.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StateFilter
    # lookup_field = ['country__name']

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

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StateFilter
    def get(self, request, **kwargs):
        queryset = self.filter_queryset(self.queryset)
        data = StateSerializer(queryset, many=True).data
        return Response(data, status=200)
    
    def patch(self, request, **kwargs):
        return Response("in the patch method of generics API View", status=200)

class StateGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = StateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StateFilter

    def get_queryset(self):
        queryset = State.objects.all()
        if self.request.method == 'PUT':
            queryset = queryset.filter(name__icontains='india')
        return queryset

