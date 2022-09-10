from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import uuid

from task.models import routine
from task.forms import RoutineForm
from task.mixins import UserRoutineAccess, DeleteRoutineMixin

class CreateRoutine(LoginRequiredMixin, FormView):
	'''
		This is the page to create a routine
	'''
	template_name = "task/routine/createRoutine.html"
	form_class = RoutineForm
	
	def form_valid(self, form):
		unsaved_form = form.save(commit= False)
		unsaved_form.owner = self.request.user
		unsaved_form.token = uuid.uuid4().hex.upper()[0:12]
		unsaved_form.save()
		form.save_m2m()
		return redirect("task:listRoutine")

class UpdateRoutine(LoginRequiredMixin, UserRoutineAccess, UpdateView):
	'''
		This is the page to update a routine
	'''
	template_name = 'task/routine/updateRoutine.html'
	fields = ["title", "detail", "token" ,"time", "days"]
	success_url = reverse_lazy('task:listRoutine')

	def get_object(self):
		return get_object_or_404(routine, token=self.kwargs['token'])

class DeleteRoutine(LoginRequiredMixin, DeleteRoutineMixin, DeleteView):
	'''
		This is the page to delete a routine
	'''
	success_url = reverse_lazy('task:listRoutine')
	template_name = "task/routine/DeleteRoutine.html"

	def get_object(self):
		object = get_object_or_404(routine, token=self.kwargs['token'])
		return object
		
class listRoutine(LoginRequiredMixin, ListView):
	'''
		This is the page to list all the routines
	'''

	template_name = 'task/routine/listRoutine.html'
	paginate_by = 2

	def get_queryset(self):
		return routine.objects.filter(owner= self.request.user).order_by("time")