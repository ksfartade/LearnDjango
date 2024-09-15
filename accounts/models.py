from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User

class CustomUser(User):
    # Add any custom fields here
    pass