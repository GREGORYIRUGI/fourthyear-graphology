# from django.db import models
# from django.contrib.auth.models import User,AbstractUser

# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=20,null=True)
#     email = models.EmailField(unique=True,null=True)
#     # avatar = models.ImageField(null = True)
#     USERNAME_FIELD = 'email'


# class Log():
#     username = models.CharField(max_length=30)
#     # query = models.Field

# models.py

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS =[]

#     # Add any other fields or methods you need

#     def __str__(self):
#         return self.email
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
