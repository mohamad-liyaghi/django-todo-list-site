from django.db import models
from accounts.models import User


class Base(models.Model):
    '''Common fields of Task, Routine and Project model'''

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
        return self.title




