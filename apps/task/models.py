from django.db import models
from accounts.models import User


class Base(models.Model):
    '''Common fields of Task, Routine and projects model'''

    class Status(models.TextChoices):
        u = ("u", "Unfinished ")
        f = ("f", "Finished")
        d = ("d", "Doing")

    title = models.CharField(max_length=120)
    detail = models.TextField()

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    token = models.CharField(max_length=12, unique=True, blank=True, null=True)

    time = models.DateTimeField()

    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


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