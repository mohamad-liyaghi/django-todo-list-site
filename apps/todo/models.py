from django.db import models
from account.models import User
from datetime import date

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    time_to_start = models.DateTimeField()
    time_to_finish = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def Is_Past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing