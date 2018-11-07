from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket


def requests(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets:requests')
    context = { 'form': form }
    return render(request, 'tickets/requests.html', context)

def dashboard(request):
    return render(request, 'tickets/dashboard.html')
