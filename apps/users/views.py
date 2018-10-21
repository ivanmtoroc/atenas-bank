from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import JsonResponse
from .forms import NewUserForm, LoginForm
from .models import Profile

@login_required
def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:new')
    else:
        form = NewUserForm()
    context = {
        'form': form,
        'profiles': Profile.list()
    }
    return render(request, 'users/new_user.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

def login_view(request):
    context = {
        'form': LoginForm()
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('users:new')
        else:
            context['error'] = 'Invalid username or password'
            return render(request, 'users/login.html', context)
    return render(request, 'users/login.html', context)

@login_required
def change_status(request):
    if request.is_ajax():
        id = request.POST.get('id', None)
        try:
            user = User.objects.get(id = id)
            user.is_active = not user.is_active
            user.save()
            if user.is_active:
                messages.success(request, 'User successfully activated')
            else:
                messages.success(request, 'User successfully deactivated')
        except User.DoesNotExist as e:
            messages.error(request, 'User does not exist')
    else:
        messages.error(request, 'Unauthorized access')
    data = {
        'url': reverse('users:new')
    }
    return JsonResponse(data)
