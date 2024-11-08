from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('event_display/', views.event_display, name='event_display'),
    
]