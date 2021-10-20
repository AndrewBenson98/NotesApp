from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


# class UserProfile(models.Model):
#     user = ForeignKey(User, on_delete=models.CASCADE)