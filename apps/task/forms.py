from django import forms
from django.forms import ModelForm
from .models import task, project, routine 

class TodoForm(ModelForm):
	class Meta:
		model = task
		fields = "__all__"
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tasks Name'}),
			'detail': forms.TextInput(attrs={'class':'form-control', 'placeholder':'write a few lines about your Task'}),
			'time_to_start': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
		}

class ProjectForm(ModelForm):
	class Meta:
		model = project
		fields = "__all__"

class ProjectTaskForm(ModelForm):
	class Meta:
		model = task
		fields = "__all__"

class RoutineForm(ModelForm):
	class Meta:
		model = routine
		fields = "__all__"