from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = NewUserForm()
    context = {
        'form': form,
        'profiles': Profile.list()
    }
    return render(request, 'users/new-user.html', context)

def login(request):
    return render(request, 'users/login.html')
