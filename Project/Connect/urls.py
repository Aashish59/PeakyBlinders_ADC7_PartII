from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',register),
    path('',homepage),
    path('adminpanel/',adminPanel),
    path('homes/',home),
    
]