from django.urls import path
from . import views

urlpatterns = [
    path('landing/',views.landing, name='landing'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('cv/', views.cv, name='cv'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact')
]
