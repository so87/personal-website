from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
path('', views.HomePage, name='home'),

]