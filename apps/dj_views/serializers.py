from rest_framework.serializers import Serializer, ModelSerializer
from .models import *

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'