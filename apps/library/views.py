from rest_framework import generics, status, viewsets
from django_filters import rest_framework as filters
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer
from .filters import BookFilter


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

class BookViewAPIView(APIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

    def get(self, request):
        queryset = Book.objects.all()

        # queryset = BookFilter(request=request.GET, queryset=queryset)
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(request, queryset, self)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

class BookViewSet(viewsets.ViewSet):
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = Book.objects.all()
        backends = [backend() for backend in self.filter_backends]
        for backend in backends:
            queryset = backend.filter_queryset(request=self.request, queryset=queryset, view=self)

        return queryset


    def retrieve(self, request, pk=None):
        book = Book.objects.get(id=pk)
        book = self.serializer_class(book)
        return Response(book.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        queryset = self.get_queryset()
        book = self.serializer_class(queryset, many=True)
        return Response(book.data, status=status.HTTP_200_OK)