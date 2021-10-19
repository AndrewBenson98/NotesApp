from django.urls import path, include
from rest_framework import routers
from . import views

router= routers.DefaultRouter()
router.register('notes',views.NoteViewSet)

urlpatterns =[path('', include(router.urls))]