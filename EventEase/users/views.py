
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth import views as auth_views
from .models import Profile


class CustomLoginView(auth_views.LoginView):
    template_name = 'login.html'  #

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')

            # Save the phone number to the Profile model associated with the user
            Profile.objects.create(user=user, phone_number=phone_number)

            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'login_registration.html', {'form': form})
