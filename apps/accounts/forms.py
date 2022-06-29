from allauth.account.forms import SignupForm
from django import forms
from accounts.models import User

import uuid

class RegisterUserForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def custom_signup(self, request, user):
        token = uuid.uuid4().hex.upper()[0:12]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.token = token
        user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', "token",'password1', 'password2')

        help_texts = {
            'username': None,
            'password1' : None,
            'password2': None,
        }

    