from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.core.mail import EmailMessage
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,ListView,View
import uuid
from .forms import RegisterUserForm
from .tokens import account_activation_token
from .mixins import AuthMixin
class register_user(CreateView):
	form_class = RegisterUserForm
	template_name =  "account/register.html"
	@transaction.atomic
	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = False
		user.token =  uuid.uuid4().hex.upper()[0:12]
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = 'Active your account'
		message = render_to_string('account/activate_account.html', {
			'user': user,
			'domain': current_site.domain,
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
		})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
					mail_subject, message, to=[to_email]
		)
		email.send()
		return HttpResponse('Please check your inboxes and confirm your email')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, ('Thank you for your email confirmation. Now you can login your account.'))
        return redirect('todo:home')
    else:
        return HttpResponse('Activation link is invalid!')

def logout_user(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, ("You Were Logged Out!"))
		return redirect('todo:home')

	else:
		return redirect("account:login")



class login_user(LoginView):
	template_name = "account/login.html"
	def get_success_url(self):
		user = self.request.user	
		return reverse_lazy('todo:home')


class Token(AuthMixin,ListView):
	template_name="account/token.html"
	def get_queryset(self):
		token = self.request.user.token
		return token

class ChangeToken(AuthMixin,View):
	def get(self,reqest):
		User.objects.filter(username=self.request.user.username).update(
			token= uuid.uuid4().hex.upper()[0:12]
		)
		return redirect("account:token")