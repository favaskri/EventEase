from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AdminLoginView



from . import views
urlpatterns = [
    
    
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout')  ,
    path('admin_login',  AdminLoginView.as_view(), name='admin_login'),
    path('user_register/', views.user_registration_view, name='user_register'),
    path('admin_register/', views.admin_registration_view, name='admin_register'),
      # Logout, redirects to homepage

    
]