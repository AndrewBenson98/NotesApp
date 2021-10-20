from django.shortcuts import render
from djoser import serializers
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
#from rest_framework import generics, mixins, views
# Create your views here.

"""
The note viewset for viewing, creating, updating, and deleting notes
"""
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class=NoteSerializer
    permission_classes = [IsAuthenticated]
    
    
    """
    Get's only the notes for the current logged in user
    """
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    """
    Sets the user as the current user when creating a new Note
    """
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)