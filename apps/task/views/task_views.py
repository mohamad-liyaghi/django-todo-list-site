from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

import uuid

from task.models import task
from task.forms import TodoForm
from task.mixins import UserTodoAccess, DeleteTodoMixin





class home_page(LoginRequiredMixin, ListView):
	'''
		This is the home page and a list of all the tasks
	'''
	template_name = 'base/home.html'
	paginate_by = 2

	def get_queryset(self):
		return  task.objects.filter(owner=self.request.user).order_by("time_to_start","done")

class updateTask(LoginRequiredMixin, UserTodoAccess, UpdateView):
	'''
		This is the page to update a task
	'''
	template_name = 'task/task/updateTask.html'
	fields = ["name", "detail", "time_to_start", "token" ,"done"]
	success_url = reverse_lazy('task:home')

	def get_object(self):
		return get_object_or_404(task, token=self.kwargs['token'])
	
class CreateTask(LoginRequiredMixin, FormView):
	'''
		This is the page to create a task
	'''
	template_name = 'task/task/createTask.html'
	form_class = TodoForm
	success_url = 'task:home'

	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.owner = self.request.user
		owner_form.token = uuid.uuid4().hex.upper()[0:12]
		owner_form.save()
		return redirect('task:home')

class DeleteTask(DeleteTodoMixin,DeleteView):
	'''
		This is the page to delete a task
	'''
	model = task
	success_url = reverse_lazy('task:home')
	template_name = "task/task/DeleteTask.html"

class SearchTask(ListView):
    model = task
    template_name = "base/search.html"

    def get_queryset(self):
        query = self.request.GET.get("nav_search")
        object_list =  task.objects.filter(Q(name__icontains=query))
        return object_list.filter(owner=self.request.user)

