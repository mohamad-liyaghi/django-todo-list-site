from django.shortcuts import redirect ,get_object_or_404
from .models import Task


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