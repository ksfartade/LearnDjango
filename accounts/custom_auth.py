from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    def authenticate_credentials(self, key):
        return super().authenticate_credentials(key)
    def authenticate(self, request):
        # Extract token from the 'X-Custom-Token' header
        token = request.headers.get('Authorization')
        print("Token received") if token else print("Token not received")
        return super().authenticate(request)
        

# class CustomTokenAuthentication(TokenAuthentication):
#     keyword = 'Bearer'