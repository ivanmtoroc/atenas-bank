from django.shortcuts import render


def hello(request):
    return render(request, 'users/hello.html')
