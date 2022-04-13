from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    token = models.CharField(max_length=12,blank=True,null=True)

