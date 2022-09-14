from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import uuid

from task.models import Task
from project.forms import ProjectForm, ProjectTaskForm
from project.models import Project


class CreateProject(LoginRequiredMixin, FormView):
    '''
        Create a new Project
    '''
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.owner = self.request.user
        form.token = uuid.uuid4().hex.upper()[0:12]
        form.save()
        return redirect("project:project_list")


class UpdateProject(LoginRequiredMixin, UpdateView):
    '''
        Update a project
    '''
    template_name = 'project/update_project.html'
    fields = ["title", "detail", "time", "status"]
    success_url = reverse_lazy('project:project_list')

    def get_object(self):
        return get_object_or_404(Project, token=self.kwargs['token'],
                                 owner=self.request.user)


class DeleteProject(LoginRequiredMixin, DeleteView):
    '''
        Delete a Project
    '''
    success_url = reverse_lazy('project:project_list')
    template_name = "project/delete_project.html"

    def get_object(self):
        object = get_object_or_404(Project, token=self.kwargs['token'], owner=self.request.user)
        return object

    def post(self, request, *args, **kwargs):
        # Check if there is any task for project to delete

        if (task:=self.get_object().task):
            task.all().delete()
            return super(DeleteProject, self).delete(request, *args, **kwargs)

        return super(DeleteProject, self).delete(request, *args, **kwargs)


class ProjectList(LoginRequiredMixin, ListView):
    '''
        List of a users project
    '''

    template_name = 'project/project_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by("status")


class ProjectTaskList(LoginRequiredMixin, ListView):
    '''
        List of task of a Project
    '''
    template_name = 'project/project_task_list.html'

    def get_queryset(self):
        project_token = self.kwargs["token"]
        project = get_object_or_404(Project, token=project_token, owner=self.request.user)

        return project.task.all()


class CreateProjectTask(LoginRequiredMixin, FormView):
    '''
        This is the page to create a task in a project
    '''
    template_name = 'project/create_project_task.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        form = form.save(commit=False)
        project_model = Project.objects.filter(token=self.kwargs['token']).first()
        form.owner = self.request.user
        form.token = uuid.uuid4().hex.upper()[0:12]
        form.save()
        project_model.task.add(form)
        return redirect('project:project_list')