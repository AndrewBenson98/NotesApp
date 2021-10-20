from django.urls import path, include
from rest_framework import routers
from . import views

router= routers.DefaultRouter()

"""
Notes urls
"""
router.register('notes',views.NoteViewSet, basename='notes')

urlpatterns =[path('', include(router.urls))]