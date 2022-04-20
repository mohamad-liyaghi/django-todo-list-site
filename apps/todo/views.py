from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DeleteView,UpdateView,FormView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

import uuid,json

from todo.models import task
from .forms import UpdateTodoForm
from .mixins import UserTodoAccess,DeleteTodoMixin
# Create your views here.
class home_page(LoginRequiredMixin,ListView):
	template_name = 'todo/home.html'
	def get_queryset(self):
		return  task.objects.filter(owner=self.request.user).order_by("done")
class updateTask(LoginRequiredMixin,UserTodoAccess,UpdateView):
	template_name = 'todo/updateTask.html'
	model =  task
	form_class = UpdateTodoForm
	success_url = 'todo:home'
	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.owner = self.request.user
		owner_form.save()
		return redirect('todo:home')
	
class CreateTask(LoginRequiredMixin,FormView):
	template_name = 'todo/createTask.html'
	form_class = UpdateTodoForm
	success_url = 'todo:home'
	def form_valid(self,form):
		owner_form = form.save(commit=False)
		owner_form.owner = self.request.user
		owner_form.token = uuid.uuid4().hex.upper()[0:12]
		owner_form.save()
		return redirect('todo:home')
class DeleteTask(DeleteTodoMixin,DeleteView):
	model = task
	success_url = reverse_lazy('todo:home')
	template_name = "todo/DeleteTask.html"

class SearchTask(ListView):
    model = task
    template_name = "search.html"
    def get_queryset(self):
        query = self.request.GET.get("nav_search")
        object_list =  task.objects.filter(Q(name__icontains=query))
        return object_list.filter(owner=self.request.user)
