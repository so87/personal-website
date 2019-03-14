from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
path('home/', views.HomePage, name='home'),
path('about/', views.AboutPage, name='about'),
path('contact/', views.ContactPage, name='contact'),
path('customers/', views.CustomersPage, name='customers'),
path('services/', views.ServicesPage, name='services'),
]