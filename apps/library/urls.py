from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookModelViewSet, basename='book_model_view_set')
router.register(r'bookset', BookViewSet, basename='book_view_set')

urlpatterns = [
    path('', BookView.as_view(), name='book_filter'),
    path('api_view/', BookViewAPIView.as_view(), name='book_filter_api_view')
]

urlpatterns += router.urls