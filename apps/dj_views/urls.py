from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('g-set', StateGenericViewSet, basename='state-generic-viewset')


urlpatterns = [
    path('get-states/', StateList.as_view(), name='get-states-list'),
    path('get-single-state/<str:name>/', StateSingle.as_view()),
    path('g-state/', StateGenericAPIView.as_view(), name='state-generic-api-view'),
    path('method/', get_state, name='method-get-states'),
    path('country/', get_countries, name = 'method-get-countries'),
    path('country-call/', get_countries_call, name = 'method-country-call'),
]

urlpatterns += router.urls