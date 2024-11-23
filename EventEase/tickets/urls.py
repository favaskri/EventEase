from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    
    path('tickets/', views.tickets, name='tickets'),
    path('purchase_tickets/<int:pk>/', views.purchase_tickets, name='purchase_tickets'),
    path('process_purchase/<int:pk>/', views.process_purchase, name='process_purchase'),
    path('success/<str:ticket_ids>/', views.ticket_success, name='ticket_success'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
]