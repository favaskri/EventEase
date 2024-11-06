from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def event_list(request):
    return render(request,'event_list_layout.html')
