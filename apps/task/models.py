from django.db import models
from accounts.models import User


class Base(models.Model):
    '''Common fields of Task, Routine and projects model'''

    title = models.CharField(max_length=120)
    detail = models.TextField()

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    token = models.CharField(max_length=12, unique=True, blank=True, null=True)

    time = models.TimeField()

    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Task(Base):
    '''Task model'''

    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    token = models.CharField(max_length=12, unique=True, blank=True)
    task = models.ManyToManyField(Task, blank=True)
    deadline = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


