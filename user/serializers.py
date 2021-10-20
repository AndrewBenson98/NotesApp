# from .models import User
from rest_framework import serializers as rfserializers
#from .models import UserProfile
from djoser import serializers
from djoser.serializers import \
    UserCreateSerializer as BaseUserCreateSerializer, \
    UserSerializer as BaseUserSerializer

class UserCreateSerialzer(BaseUserCreateSerializer):
    
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']


class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields=['id','username','email','first_name','last_name']


# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserCreateSerialzer()
#     class Meta:
#         model = UserProfile
#         fields =['id','user']