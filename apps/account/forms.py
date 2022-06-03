from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django import forms
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',"token",'password1', 'password2')
        help_texts = {
            'username': None,
            'password1' : None,
            'password2': None,
        }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = "Enter a valid password like: 4020TrKu (dont use this!)"
        self.fields['password2'].help_text = 'confirm your password'
