from django.views.generic import DetailView, View
from django.shortcuts import redirect
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User


class Token(LoginRequiredMixin, DetailView):
    '''Show users token'''
    template_name = "accounts/token.html"

    def dispatch(self, request, *args, **kwargs):
        # Check if user has a token
        if request.user.is_authenticated and request.user.token:
            return super().dispatch(request, *args, **kwargs)

        return redirect("accounts:token-generator")

    def get_object(self):
        token = self.request.user.token
        return token


class TokenGenerator(LoginRequiredMixin, View):
    '''Token generator page'''

    def get(self, request):
        token = uuid.uuid4().hex.upper()[0:12]
        if not User.objects.filter(token=token):
            self.request.user.token = token
            self.request.user.save()
            return redirect("accounts:token")
        return redirect("accounts:token-generator")