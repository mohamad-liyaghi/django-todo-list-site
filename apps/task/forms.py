from django import forms
from django.forms import ModelForm
from .models import Task

class TodoForm(ModelForm):
	class Meta:
		model = Task
		fields = "__all__"
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tasks Name'}),
			'detail': forms.TextInput(attrs={'class':'form-control', 'placeholder':'write a few lines about your Task'}),
			'time_to_start': forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD HH:MM:SS'}),
		}



