from django.shortcuts import redirect,get_object_or_404
from .models import task

class UserTodoAccess():
	def dispatch(self, request, pk, *args, **kwargs):
		self_task = get_object_or_404(task, pk=pk)
		if  self_task.owner  == self.request.user:
			return super().dispatch(request, *args, **kwargs)
		else:
			return redirect("todo:home")

