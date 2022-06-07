from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, View


import uuid

from account.models import User
from .forms import RegisterUserForm
from .mixins import AuthMixin, RegitsterMixin


class register_user(RegitsterMixin,CreateView):
	'''
		Register page
	'''
	form_class = RegisterUserForm
	template_name = "account/register.html"

	@transaction.atomic
	def form_valid(self,  form):
		user = form.save(commit=False)
		user.token =  uuid.uuid4().hex.upper()[0:12]
		user.username = user.first_name + user.last_name + uuid.uuid4().hex.upper()[0:4]
		user.save()
		login(self.request, user)
		messages.success(self.request, ("You Were registered successfully!"))
		return redirect('todo:home')

	def form_invalid(self, form):
		messages.success(self.request, ("Sth went wrong, please try again..."))
		return redirect('account:register')


def logout_user(request):
	'''
		Login page
	'''

	if request.user.is_authenticated:
		logout(request)
		messages.success(request, ("You Were Logged Out!"))
		return redirect('todo:home')

	else:
		return redirect("account:login")



class login_user(LoginView):
	'''
		Logout page
	'''
	template_name = "account/login.html"
	def get_success_url(self):
		user = self.request.user	
		return redirect('todo:home')


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