from django.shortcuts import render
from events.models import Event

# Create your views here.

def tickets(request):
    event_details=Event.objects.all()

    return render(request, 'tickets_layout.html' ,{'event_details':event_details})

def purchase_tickets(request):
    return render(request, 'purchase_ticket_layout.html')
