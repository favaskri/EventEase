from django.shortcuts import render,get_object_or_404,redirect
from events.models import Event
from .models import Ticket

# Create your views here.

def tickets(request):
    event_details=Event.objects.all()

    return render(request, 'tickets_layout.html' )


def purchase_tickets(request, pk):
    event = get_object_or_404(Event, pk=pk)
    quantity = 1  # Default quantity
    total_price = event.ticket_price  # Default total price

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1 or quantity > 10:
            return render(request, 'error.html', {'message': 'Invalid quantity. Please select between 1 and 10 tickets.'})
        total_price = event.ticket_price * quantity

    return render(request, 'purchase_ticket_layout.html', {
        'event_ticket': event,
        'quantity': quantity,
        'total_price': total_price,
    })


def ticket_success(request, ticket_id):
    return render(request, 'ticket_success.html', {'ticket_id': ticket_id})
