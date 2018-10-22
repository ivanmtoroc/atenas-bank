from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(min_length = 4, max_length = 20)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'cedula', 'first_name', 'last_name', 'email', 'phone', 'address', 'position']
