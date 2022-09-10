from django.shortcuts import redirect ,get_object_or_404
from .models import Task, project, routine


class UserTodoAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_task = get_object_or_404(Task, token= token)
		if  self_task.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")

class DeleteTodoMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_task = get_object_or_404(Task, token= token)
		if self_task.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")


class UserProjectAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_project = get_object_or_404(project, token= token)
		if  self_project.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")

class DeleteProjectMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_project = get_object_or_404(project, token= token)
		if self_project.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")

class UserRoutineAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_routine = get_object_or_404(routine, token= token)
		if  self_routine.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")

class DeleteRoutineMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_routine = get_object_or_404(routine, token= token)
		if self_routine.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("task:home")


#Token mixin
class AuthMixin():
    '''
        This class let authenticated people to create new token
    '''
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:login")

class RegitsterMixin():
    '''
        dont let authenticated users to login/register
    '''
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("task:home")