from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import * 


class User(AbstractUser):
    username =None
    phone_number=models.CharField(max_length=12,unique=True)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]

    objects=UserManager()
