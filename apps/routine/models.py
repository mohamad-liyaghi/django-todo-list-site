from django.db import models
from task.models import Base


class Routine(Base):
    '''Routine model that inherits base model'''

    class Choises(models.TextChoices):
        once = ("o", "Once")
        daily = ("d", "Daily")
        mon_to_fri = ("m", "Mon To Fri")


    repeat = models.CharField(max_length=1, choices=Choises.choices, default=Choises.once)

    def __str__(self):
        return self.title