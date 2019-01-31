from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length = 4, max_length = 20)
    password = forms.CharField(max_length = 30, widget = forms.PasswordInput)
