from rest_framework import serializers
from .models import SY

class SYSerializer(serializers.ModelSerializer):
    class Meta:
        model = SY
        fields = '__all__'
