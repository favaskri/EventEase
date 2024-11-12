from django.shortcuts import render,redirect,get_object_or_404
from .models import Event,Profile
from .forms import EventForm
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            event=form.save(commit=False)
            profile,created=Profile.objects.get_or_create(user=request.user)
            event.user=profile
            form.save()
           
            return redirect('display_event') 
    else:
        form = EventForm()  # Initialize an empty form on GET request

    # Render the form, with validation errors if POST data was invalid
    return render(request, 'create_event_layout.html', {'form': form})

    
def event_display(request):
    event_requests = Event.objects.all()
    print(event_requests)
    return render(request,'event_display_layout.html', {'event_requests': event_requests})


@login_required
def event_list(request):
    # Retrieve all venue requests (events) from the database
    user=request.user
    profile , created =Profile.objects.get_or_create(user=user)
    event_list = Event.objects.filter(user=profile)
    print(event_list)
    return render(request,'event_list_layout.html',{'event_list':event_list})

def update_event(request,pk):
    event=get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        print(event)
        form = EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
                   
    else:
        form = EventForm(instance=event)  

    return render(request, 'update_event_layout.html', {'form': form})



def delete_event(request,pk):
    # Retrieve all venue requests (events) from the database
    user=request.user
    profile  =Profile.objects.get(user=user)
    event=get_object_or_404(Event,pk=pk,user=profile)
    
    
    if request.method == 'POST':
        event.delete()
        print(event_list)
        return redirect('event_list')
      
    return redirect('event_list')
    


