from django.urls import path
from . import views
urlpatterns = [
    
    path('rent_venue/', views.rent_venue, name='rent_venue'),
    
]