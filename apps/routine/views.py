from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import uuid

from routine.models import Routine
from routine.forms import RoutineForm


class CreateRoutine(LoginRequiredMixin, FormView):
    '''
        Create a new routine
    '''
    template_name = "routine/create_routine.html"
    form_class = RoutineForm

    def form_valid(self, form):
        form = form.save(commit=False)
        form.owner = self.request.user
        form.token = uuid.uuid4().hex.upper()[0:12]
        form.save()
        return redirect("routine:routine_list")


class UpdateRoutine(LoginRequiredMixin, UpdateView):
    '''
        This is the page to update a routine
    '''
    template_name = 'routine/update_routine.html'
    fields = ["title", "detail", "time", "repeat"]
    success_url = reverse_lazy('routine:routine_list')

    def get_object(self):
        return get_object_or_404(Routine, token=self.kwargs['token'],
                                 owner=self.request.user)


class DeleteRoutine(LoginRequiredMixin, DeleteView):
    '''
        Delete a routine
    '''
    success_url = reverse_lazy('routine:routine_list')
    template_name = "routine/delete_routine.html"

    def get_object(self):
        object = get_object_or_404(Routine, token=self.kwargs['token'], owner=self.request.user)
        return object


class RoutineList(LoginRequiredMixin, ListView):
    '''
        Routine list
    '''

    template_name = 'routine/routine_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Routine.objects.filter(owner=self.request.user).order_by("time")