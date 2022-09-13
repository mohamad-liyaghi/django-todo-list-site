from django import forms
from accounts.models import User

import uuid

class RegisterUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', "token",'password')

        help_texts = {
            'password1' : None,
            'password2': None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.token = uuid.uuid4().hex.upper()[0:12]
        user.save()
        return user

    