from django.shortcuts import redirect,get_object_or_404
from .models import task, project, routine


class UserTodoAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_task = get_object_or_404(task, token= token)
		if  self_task.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")

class DeleteTodoMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_task = get_object_or_404(task, token= token)
		if self_task.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")


class UserProjectAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_project = get_object_or_404(project, token= token)
		if  self_project.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")

class DeleteProjectMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_project = get_object_or_404(project, token= token)
		if self_project.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")

class UserRoutineAccess():
	def dispatch(self, request, token, *args, **kwargs):
		self_routine = get_object_or_404(routine, token= token)
		if  self_routine.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")

class DeleteRoutineMixin():
	def dispatch(self, request, token, *args, **kwargs):
		self_routine = get_object_or_404(routine, token= token)
		if self_routine.owner == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")