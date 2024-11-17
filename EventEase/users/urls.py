from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    
    
    path('register/', views.register, name='login_registration'),  # User registration page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout')  
      # Logout, redirects to homepage

    
]