from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_event/', views.create_event, name='create_event'),
    path('display_event/', views.event_display, name='display_event'),
    path('admin_event_list/', views.admin_event_list, name='admin_event_list'),
    path('admin_ticket_list/', views.admin_ticket_list, name='admin_ticket_list'),
    path('admin_users_list/', views.admin_users_list, name='admin_users_list'),
    path('update_event/<int:pk>/', views.update_event, name='update_event'),
    path('delete_event/<int:pk>/', views.delete_event, name='delete_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    
]