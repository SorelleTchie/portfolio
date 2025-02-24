from django.urls import path
from . import views

urlpatterns = [
    path('landing/',views.landing, name='landing'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact')
]
