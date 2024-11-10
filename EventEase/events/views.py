from django.shortcuts import render,redirect
from registrations.models import VenueRequest
from .forms import EventForm
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    return render(request,'index.html')

# @login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the event display page or any URL name you have defined for this page
            return redirect('display_event')  # use the URL name, not the template file name
    else:
        form = EventForm()  # Initialize an empty form on GET request

    # Render the form, with validation errors if POST data was invalid
    return render(request, 'rent_venue_layout.html', {'form': form})

def event_display(request):
    # Retrieve all venue requests (events) from the database
    venue_requests = VenueRequest.objects.all()
    print(venue_requests)
    return render(request,'event_display_layout.html', {'venue_requests': venue_requests})








