from django.urls import path
from .views import *


urlpatterns = [
    path('get-states/', StateList.as_view(), name='get-states-list'),
    path('get-single-state/<str:name>/', StateSingle.as_view()),
    path('g-state/', StateGenericAPIView.as_view(), name='state-generic-api-view'),
]