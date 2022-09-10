from django.views.generic import ListView, View

import uuid

from accounts.models import User
from task.mixins import AuthMixin

class Token(AuthMixin,ListView):
	'''
		Token page
	'''
	template_name="account/token.html"
	def get_queryset(self):
		token = self.request.user.token
		return token

class ChangeToken(AuthMixin,View):
	'''
		Token generator page
	'''
	def get(self,reqest):
		User.objects.filter(username=self.request.user.username).update(
			token= uuid.uuid4().hex.upper()[0:12]
		)
		return redirect("account:token")