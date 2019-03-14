from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.
def HomePage(request):
    return render(request, "home.html")

def AboutPage(request):
    return render(request, "about.html")

def ContactPage(request):
    return render(request, "contact.html")

def CustomersPage(request):
    return render(request, "customers.html")

def ServicesPage(request):
    return render(request, "services.html")