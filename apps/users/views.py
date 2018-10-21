from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import JsonResponse
from .forms import NewUserForm, LoginForm
from .models import Profile


@login_required
def users(request):
    context = {
        'profiles': Profile.list()
    }
    if request.method == 'POST':
        form_create = NewUserForm(request.POST)
        if form_create.is_valid():
            form_create.save()
            return redirect('users:crud')
        context['new'] = True
    else:
        form_create = NewUserForm()
        form_update = NewUserForm()
    context['form_create'] = form_create
    return render(request, 'users/users.html', context)

@login_required
def delete(request):
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
        'url': reverse('users:crud')
    }
    return JsonResponse(data)


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
            return redirect('users:crud')
        else:
            context['error'] = 'Invalid username or password'
            return render(request, 'users/login.html', context)
    return render(request, 'users/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
