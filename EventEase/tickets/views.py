from django.shortcuts import render

# Create your views here.

def tickets(request):
    return render(request, 'tickets_layout.html')

def purchase_tickets(request):
    return render(request, 'purchase_ticket_layout.html')
