from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('accounts/',accounts),
    path('signup/',register),
    path('delete/<int:id>', delete),
    path('',home),
    path('adminpanel/',adminPanel),
     
]