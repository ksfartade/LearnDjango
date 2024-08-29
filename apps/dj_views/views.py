from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import generics
from rest_framework import mixins, viewsets

from accounts.custom_auth import CustomTokenAuthentication
from .permissions import BlocklistPermission
from .serializers import *
from .views import *
from .filters import *
import django_filters

# @login_required
@api_view(['GET', 'POST'])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([BlocklistPermission])
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


@csrf_exempt
@api_view(['GET', 'POST'])
def get_countries_call(request, **kwargs):
    if request.method == "GET":
        view = StateList()
        view = view.as_view()
        response = view(request._request)
        return response
    else:
        print("request method is not GET")
        return HttpResponseRedirect('/views/g-state/')


class StateList(generics.ListAPIView):
    pagination_class = None
    serializer_class = StateSerializer
    queryset = State.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StateFilter
    permission_classes = [BlocklistPermission]
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
    permission_classes = [AllowAny]

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = StateFilter
    def get(self, request, **kwargs):
        print("user: ", request.user)
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
