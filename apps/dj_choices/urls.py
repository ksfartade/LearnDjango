from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SYViewSet

router = DefaultRouter()
router.register('viewset', SYViewSet, basename='SY_model_viewset')

urlpatterns = []

urlpatterns += router.urls