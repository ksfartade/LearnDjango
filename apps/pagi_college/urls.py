from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'viewset', ViewSetView, basename='pagi_viewsetview')
router.register(r'modelviewset', ModelViewSetView, basename='pagi_modelviewset')

urlpatterns = [
    path('generics/', GenericsView.as_view(), name='pagi_generics'),
    path('api_view/', APIViewView.as_view(), name='pagi_apiview')
]

urlpatterns += router.urls