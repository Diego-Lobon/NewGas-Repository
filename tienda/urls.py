from django.urls import path
from tienda.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('home', HomePageView.as_view(), name="index"),

]