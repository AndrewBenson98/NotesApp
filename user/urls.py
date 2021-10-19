from django.urls import path, include
# from rest_framework import routers
# from . import views

# router= routers.DefaultRouter()
# router.register('users',views.UserViewSet)

urlpatterns =[
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    ]