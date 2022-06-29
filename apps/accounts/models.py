from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # telegram userid (for telegram service)
    telegram_id = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=12,blank=True,null=True)

