from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',register),
    path('',home),
    path('adminpanel/',adminPanel),   
]