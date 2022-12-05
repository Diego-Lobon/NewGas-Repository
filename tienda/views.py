from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from tienda.models import *
#from tienda.forms import *
#from ipware import get_client_ip

from django.db.models import Sum




#import stripe

from django.conf import settings
from django.urls import reverse

class HomePageView(TemplateView):
    
    template_name = 'index.html'
