from django.db import models
from accounts.models import User
from datetime import date

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=12,unique=True,blank=True,null=True)
    time_to_start = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=12, unique=True, blank=True)
    task = models.ManyToManyField(task, blank=True)
    deadline = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class week(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class routine(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=12, unique=True, blank=True)
    time = models.TimeField()
    days = models.ManyToManyField(week, blank=True)

    def __str__(self):
        return self.title