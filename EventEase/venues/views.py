from django.shortcuts import render

# Create your views here.
def rent_venue(request):
    return render(request,'rent_venue_layout.html')
