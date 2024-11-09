from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_event/', views.create_event, name='create_event'),
     path('display_event/', views.event_display, name='display_event'),
     path('accounts/login/', views.CustomLoginView.as_view(), name='login')
    
]