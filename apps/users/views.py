from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import JsonResponse
from .forms import UserForm, LoginForm
from .models import User


@login_required
def users(request):
    context = {
        'users': User.list()
    }
    form_create = UserForm()
    form_update = UserForm()
    if request.method == 'POST':
        if 'create' in request.POST:
            form_create = UserForm(request.POST)
            if form_create.is_valid():
                form_create.save()
                return redirect('users:crud')
            context['new'] = True
        else:
            id = request.POST.get('id', None)
            print('Identificador:', id)
            user = User.objects.get(id = id)
            context['id'] = id
            if 'update-get' in request.POST:
                form_update = UserForm(instance = user)
                context['update'] = True
            else:
                form_update = UserForm(request.POST, instance = user)
                if form_update.is_valid():
                    form_update.save()
                    return redirect('users:crud')
                context['update'] = True
    context['form_create'] = form_create
    context['form_update'] = form_update
    return render(request, 'users/users.html', context)


def modifyPizza(request, id):
	pizza = Pizza.objects.get(id = id)
	if request.method == 'GET':
		form = RegisterPizza(instance = pizza)
	else:
		form = RegisterPizza(request.POST, request.FILES, instance = pizza)
		if form.is_valid():
			form.save()
			messages.success(request, 'Pizza modificada exitosamente')
			return redirect('products:pizza')
		else:
			messages.error(request, 'Pizza no modificada')
	context = {
		'form': form,
		'pizza': pizza
	}
	return render(request, 'products/modify_pizza.html', context)







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
