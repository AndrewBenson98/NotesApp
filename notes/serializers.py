from rest_framework.fields import ReadOnlyField
from .models import Note
from rest_framework import serializers
from django.contrib.auth import get_user_model

#The user model for this application
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
        
class NoteSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user=UserSerializer()
    class Meta:
        model =Note
        fields = ['id','title','text', 'user']

