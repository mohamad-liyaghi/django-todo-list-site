from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

import uuid

from task.models import task
from task.forms import TodoForm
from task.mixins import UserTodoAccess, DeleteTodoMixin



class TaskList(LoginRequiredMixin, ListView):
    '''
        List of all tasks
    '''

    template_name = 'task/task_list.html'
    paginate_by = 2

    def get_queryset(self):
        return task.objects.filter(owner=self.request.user).order_by("time_to_start", "done")


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


class UpdateTask(LoginRequiredMixin, UserTodoAccess, UpdateView):
    '''
        Update a task
    '''

    template_name = 'task/update_task.html'
    fields = ["name", "detail", "time_to_start", "token", "done"]
    success_url = reverse_lazy('task:home')

    def get_object(self):
        return get_object_or_404(task, token=self.kwargs['token'])



class DeleteTask(LoginRequiredMixin, DeleteTodoMixin, DeleteView):
    '''
        Delete a task
    '''

    model = task
    success_url = reverse_lazy('task:home')
    template_name = "task/delete_task.html"

    def get_object(self):
        return get_object_or_404(task, token=self.kwargs["token"], owner=self.request.user)


class SearchTask(ListView):
    model = task
    template_name = "base/search.html"

    def get_queryset(self):
        query = self.request.GET.get("nav_search")
        object_list = task.objects.filter(Q(name__icontains=query))
        return object_list.filter(owner=self.request.user)

