from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SYViewSet, DepViewSet

router = DefaultRouter()
router.register('viewset', SYViewSet, basename='SY_model_viewset')
router.register('dep_viewset', DepViewSet, basename='dep_view_set')

urlpatterns = []

urlpatterns += router.urls