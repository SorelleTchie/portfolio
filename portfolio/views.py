from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.views import View


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
    
 
    
    
  
