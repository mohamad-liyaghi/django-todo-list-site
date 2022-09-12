from django.db import models
from task.models import Base, Task


class Project(Base):
    '''Model for creating projects'''

    # tasks of a project
    task = models.ManyToManyField(Task, blank=True, related_name="project_task")

    def __str__(self):
        return self.titlle