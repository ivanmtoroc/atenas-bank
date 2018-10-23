from django.shortcuts import render


def requests(request):
    return render(request, 'tickets/requests.html', {})


def dashboard(request):
    return render(request, 'tickets/dashboard.html', {})
