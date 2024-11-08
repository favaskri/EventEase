from django.shortcuts import render
from registrations.models import VenueRequest

# Create your views here.

def index(request):
    return render(request,'index.html')

def event_display(request):
    # Retrieve all venue requests (events) from the database
    venue_requests = VenueRequest.objects.all()
    print(venue_requests)
    return render(request,'event_display_layout.html', {'venue_requests': venue_requests})



