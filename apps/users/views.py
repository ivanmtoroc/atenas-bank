from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('users:users')
    context = { 'form': LoginForm() }
    return render(request, 'users/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
