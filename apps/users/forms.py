from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(min_length = 4, max_length = 20)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)

class NewUserForm(forms.Form):
    username = forms.CharField(min_length = 4, max_length = 20)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    password_confirmation = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        query = User.objects.filter(username = username).exists()
        if query:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation do not match')
        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user = user)
        profile.save()
