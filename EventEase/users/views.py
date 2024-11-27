from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages  # Import the messages module
from .user_forms import UserRegistrationForm
from django.contrib.auth import views as auth_views
from .models import Profile
from .admin_forms import AdminRegistrationForm
from django.contrib.auth.views import LoginView
from .admin_forms import AdminLoginForm


class CustomLoginView(auth_views.LoginView):
    print('login done ')
    template_name = 'login.html'



class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = AdminLoginForm


def custom_logout(request):
    logout(request)
    return redirect('index')



def admin_login(request):
    return render(request,'admin_login.html')



def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'login_registration.html', {'form': form})

def admin_registration_view(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_login')  # Redirect to admin login after successful registration
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_login_registration.html', {'form': form})



