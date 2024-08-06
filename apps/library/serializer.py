from rest_framework import serializers
from .models import *

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    college = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = [field.name for field in Author._meta.fields ] + ['college']
    
    def get_college(self, obj):
        college = EducationSerializer(obj.institute)
        return college.data

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'
