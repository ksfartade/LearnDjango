from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .pagination import *
# Create your views here.

class APIViewView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Subject.objects.all()
        paginator = CustomPageNumberPagination()
        # paginator.page_size = request.query_params.get('page_size', 5)
        page = paginator.paginate_queryset(queryset, request=request, view=self)
        data = SubjectSerializer(page, many=True).data
        return paginator.get_paginated_response(data)


class GenericsView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # pagination_class = None


class ViewSetView(viewsets.ViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = CustomPageNumberPagination
    def list(self, request):
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset=self.queryset, request=request, view=self)
        data = SubjectSerializer(page, many=True).data
        return paginator.get_paginated_response(data)


class ModelViewSetView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer