from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages  # Import the messages module
from .forms import RegistrationForm
from django.contrib.auth import views as auth_views
from .models import Profile

class CustomLoginView(auth_views.LoginView):
    print('login done ')
    template_name = 'login.html'

def custom_logout(request):
    logout(request)
    return redirect('index')




def register(request):
    print("Register view called")  # Debug print

    if request.method == 'POST':
        print("POST method detected")
        print(f"POST data: {request.POST}")

        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug print
            user = form.save()
            print("User before saving:", user)

            phone_number = form.cleaned_data.get('phone_number')
            user_role = form.cleaned_data.get('role')

            print(f"User role: {user_role}, Phone number: {phone_number}")  # Debug print


            # Save the phone number to the Profile model associated with the user
            Profile.objects.create(user=user, phone_number=phone_number)

            if user_role== 'Admin':
                user.is_staff=True
                user.save()

            # Log the user in and add a success message
            login(request, user)
            messages.success(request, "You have successfully registered and are now logged in.")
            return redirect('login_registration')
        else:
            print("Form errors:", form.errors)  # Debug errors
    else:
        form = RegistrationForm()

    return render(request, 'login_registration.html', {'form': form})
