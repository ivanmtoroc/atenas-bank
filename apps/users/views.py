from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:signup')
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'users/new-user.html', context)
