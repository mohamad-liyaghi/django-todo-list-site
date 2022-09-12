from django.forms import ModelForm
from project.models import Project
from task.models import Task


class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = "__all__"

class ProjectTaskForm(ModelForm):
	class Meta:
		model = Task
		fields = "__all__"