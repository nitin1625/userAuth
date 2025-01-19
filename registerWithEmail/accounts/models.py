from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import * 



class customUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    otp=models.CharField(max_length=6,blank=True)
    is_verified=models.BooleanField(default=False,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=UserManager()

    def __str__(self):
        return self.email





