from django.shortcuts import render,get_object_or_404,redirect
from events.models import Event
from .models import Ticket
from django.http import JsonResponse
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def tickets(request):
    event_details=Event.objects.all()

    return render(request, 'tickets_layout.html' )

@login_required
def purchase_tickets(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'purchase_ticket_layout.html', {'event_ticket': event})




def process_purchase(request, pk):
    
    event = get_object_or_404(Event, pk=pk)
    

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1 or quantity > 10:
            return render(request, 'error.html', {'message': 'Invalid quantity. Please select between 1 and 10 tickets.'})
        

        if event.available_tickets < quantity:
            return render(request, 'error.html', {'message': 'Not enough tickets available for this event.'})
        
        total_price = event.ticket_price * quantity

        

        if event.available_tickets < 0:  
            event.available_tickets = 0
            event.save()
        
        print(f"Before transaction: Available tickets: {event.available_tickets}")


        with transaction.atomic():
            if event.available_tickets >= quantity:
                event.available_tickets -= quantity
                event.save()
            
            tickets=[]
            for _ in range(quantity):
                ticket=Ticket.objects.create(event=event, user=request.user)
                tickets.append(ticket.id)
                print(tickets)
            # else:
            #     return render(request, 'error.html', {'message': 'Tickets sold out!'})
        

        print(f"After transaction: Available tickets: {event.available_tickets}")

        response_data = {
                'message': 'Purchase successful',
                'quantity': quantity,
                'total_price': total_price,
                'redirect_url': reverse('ticket_success', args=[','.join(map(str, tickets))]),
            }

            # Return the JSON response
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
    






# from .models import Ticket

def ticket_success(request, ticket_ids):
    ticket_ids_list = ticket_ids.split(',')
    print("Ticket IDs:", ticket_ids_list)

    # Fetch all tickets based on the IDs
    tickets = Ticket.objects.filter(id__in=ticket_ids_list)
    print("Fetched Tickets:", tickets)

    # Check if tickets have valid prices
    for ticket in tickets:
        print(f"Ticket {ticket.id} Price: {ticket.price}")

    # Calculate the total price
    total_price = sum(float(ticket.price) for ticket in tickets)

    # Pass the total price to the template
    return render(request, 'ticket_success.html', {'ticket_ids': ticket_ids_list, 'total_price': total_price})
