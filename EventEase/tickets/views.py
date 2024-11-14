from django.shortcuts import render,get_object_or_404
from events.models import Event

# Create your views here.

def tickets(request):
    event_details=Event.objects.all()

    return render(request, 'tickets_layout.html' )

def purchase_tickets(request,pk):
    event_ticket=get_object_or_404(Event,pk=pk)
    print(event_ticket.ticket_price)
    return render(request, 'purchase_ticket_layout.html',{'event_ticket':event_ticket})
