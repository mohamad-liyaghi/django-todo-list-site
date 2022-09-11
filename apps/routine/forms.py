from django import  forms
from routine.models import Routine

class RoutineForm(forms.ModelForm):
	class Meta:
		model = routine
		fields = "__all__"