from django.forms import ModelForm
from project.models import Project
from task.models import Task


class ProjectForm(ModelForm):
    """A form for creating projects"""

	class Meta:
		model = Project
		fields = "__all__"

class ProjectTaskForm(ModelForm):
    """A form for creating tasks for project"""

	class Meta:
		model = Task
		fields = "__all__"