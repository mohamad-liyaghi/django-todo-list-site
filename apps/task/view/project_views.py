from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import uuid

from task.models import task, project
from task.forms import  ProjectForm, ProjectTaskForm
from task.mixins import UserProjectAccess, DeleteProjectMixin


class CreateProject(LoginRequiredMixin, FormView):
	'''
		This is the page to create a project
	'''
	template_name = "task/project/createProject.html"
	form_class = ProjectForm

	def form_valid(self, form):
		form = form.save(commit= False)
		form.owner = self.request.user
		form.token = uuid.uuid4().hex.upper()[0:12]
		form.save()
		return redirect("task:listProject")

class UpdateProject(LoginRequiredMixin, UserProjectAccess, UpdateView):
	'''
		This is the page to update a project
	'''
	template_name = 'task/project/updateProject.html'
	fields = ["name", "detail", "deadline" ,"status", "token"]
	success_url = reverse_lazy('task:listProject')

	def get_object(self):
		return get_object_or_404(project, token=self.kwargs['token'])

class DeleteProject(LoginRequiredMixin, DeleteProjectMixin, DeleteView):
	'''
		This is the page to delete a project
	'''
	success_url = reverse_lazy('task:listProject')
	template_name = "task/project/DeleteProject.html"
	
	def get_object(self):
		object = get_object_or_404(project, token=self.kwargs['token'])
		object.task.all().delete()
		return object


class listProject(LoginRequiredMixin, ListView):
	'''
		This is the page to list all the projects
	'''

	template_name = 'task/project/listProject.html'
	paginate_by = 2

	def get_queryset(self):
		return  project.objects.filter(owner=self.request.user).order_by("status")


class ListProjectTask(LoginRequiredMixin, ListView):
	'''
		This is the page to list all the tasks of a project
	'''
	template_name = 'task/project/listProjectTask.html'
	def get_queryset(self):
		project_token = self.kwargs["token"]
		return task.objects.filter(project__token= project_token).order_by("time_to_start","done")


class CreateProjectTask(LoginRequiredMixin, FormView):
	'''
		This is the page to create a task in a project
	'''
	template_name = 'task/project/createProjectTask.html'
	form_class = ProjectTaskForm

	def form_valid(self, form):
		form = form.save(commit= False)
		project_model = project.objects.filter(token=self.kwargs['token']).first()
		form.owner = self.request.user
		form.token = uuid.uuid4().hex.upper()[0:12]
		form.save()
		project_model.task.add(form)
		return redirect('task:listProject')