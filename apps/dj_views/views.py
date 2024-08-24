from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods, require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect, reverse

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework import mixins, viewsets

from .serializers import *
from .views import *
from .filters import *
import django_filters

# @login_required
# @api_view(['GET', 'POST'])
def get_state(request, **kwargs):
    if request.method == 'GET':
        queryset = State.objects.all()
        data = StateSerializer(queryset, many=True).data
        return JsonResponse(data, status=200, safe=False)
    else:
        return JsonResponse({"error": "Invalid method type, Please use get method only"}, status=400)

# @require_http_methods(['PUT'])
@csrf_exempt
def get_countries(request, **kwargs):
    if request.method == "GET":
        queryset = Country.objects.all()
        data = CountrySerializer(queryset, many=True).data
        return JsonResponse(data=data, status=200, safe=False)
    else:
        print("get_countries method is not GET")
        response = HttpResponseRedirect('/views/g-state/')
        print("type of httpresponseredirect: ", type(response), 'data: ', response.status_code)

        response = redirect('/views/g-state/')
        print("type of redirect: ", type(response), 'data: ', type(response.content))
        return response


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
    
    @action(methods=['GET'], detail=True)
    @login_required
    def get_state(self, request, pk=None, **kwargs):
        obj = self.get_object()
        data = StateSerializer(obj).data
        return Response(data, status=200)
