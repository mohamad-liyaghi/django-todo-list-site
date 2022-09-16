from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

import uuid

from task.models import Task
from task.forms import TodoForm



class TaskList(LoginRequiredMixin, ListView):
    '''
        List of all tasks
    '''

    template_name = 'task/task_list.html'
    paginate_by = 2
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user
        ).order_by("time", "status")


class CreateTask(LoginRequiredMixin, FormView):
    '''
        Create a new task
    '''

    template_name = 'task/create_task.html'
    form_class = TodoForm
    success_url = 'task:home'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.owner = self.request.user
        form.token = uuid.uuid4().hex.upper()[0:12]
        form.save()
        return redirect('task:home')



class UpdateTask(LoginRequiredMixin, UpdateView):
    '''
        Update a task
    '''

    template_name = 'task/update_task.html'
    fields = ["title", "detail", "time", "status"]
    success_url = reverse_lazy('task:home')

    def get_object(self):
        return get_object_or_404(Task, token=self.kwargs['token'],
                                 owner=self.request.user)



class DeleteTask(LoginRequiredMixin, DeleteView):
    '''
        Delete a task
    '''

    model = Task
    success_url = reverse_lazy('task:home')
    template_name = "task/delete_task.html"

    def get_object(self):
        return get_object_or_404(Task, token=self.kwargs["token"],
                                 owner=self.request.user)


class SearchTask(ListView):
    model = Task
    template_name = "base/task_list.html"
    context_object_name = "task"

    def get_queryset(self):
        query = self.request.GET.get("nav_search")

        object = Task.objects.filter(Q(title__icontains=query)
                                          & Q(owner=self.request.user))

        return object

