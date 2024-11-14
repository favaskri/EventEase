from django.urls import path
from . import views
urlpatterns = [
    
    path('tickets/', views.tickets, name='tickets'),
    path('purchase_tickets/<int:pk>/', views.purchase_tickets, name='purchase_tickets'),
    
]