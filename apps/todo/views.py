from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import task
# Create your views here.
class home_page(LoginRequiredMixin,ListView):
	template_name = 'todo/home.html'
	def get_queryset(self):
		return  task.objects.filter(owner=self.request.user).order_by("done")
class detail(LoginRequiredMixin,DetailView):
	template_name = 'todo/detail.html'
	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(task, pk=pk)