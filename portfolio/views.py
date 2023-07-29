from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def landing(request):
    return render(request,"landing.html" )

def aboutme(request):
    return render(request, "aboutme.html")

def projects(request):
    return render(request, "projects.html")

def cv(request):
    return render(request,"cv.html")

def contact(request):
    return render(request, "contact.html")
    
    
    
    """if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'Contact Form Message',
                f'Message from {name} <{email}>:\n\n{message}',
                email,
                  ['sorelletchie@gmail.com'],  # Change to your email address
            )
            
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form}) """
  
