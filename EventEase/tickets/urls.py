from django.urls import path
from . import views
urlpatterns = [
    
    path('tickets/', views.tickets, name='tickets'),
    path('purchase_tickets/<int:pk>/', views.purchase_tickets, name='purchase_tickets'),
    path('success/<int:ticket_id>/', views.ticket_success, name='ticket_success')
    
]