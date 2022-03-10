from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DeleteView,UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 	
from .models import task
from .forms import UpdateTodoForm
from .mixins import UserTodoAccess
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
		owner_form.save()
		return redirect('todo:home')
class DeleteTask(DeleteView):
	model = task
	success_url = reverse_lazy('todo:home')
	template_name = "todo/DeleteTask.html"