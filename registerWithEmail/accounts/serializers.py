from rest_framework import serializers
from .models import customUser

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model=customUser
        fields=['email','password','is_verified']


class VerifyAccountSerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
    try:
        pass
    except Exception as e :
        print(e)
