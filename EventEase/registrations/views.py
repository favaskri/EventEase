from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.



def create_account(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        company_organization = request.POST.get("company_organization")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'account_setup.html')

        # Process the form data here (e.g., save to the database, send email, etc.)

        # Redirect to a success page or render a success message
        return redirect('success')  # or render(request, 'success_page.html')
    
    return render(request, 'rent_venue_layout.html')