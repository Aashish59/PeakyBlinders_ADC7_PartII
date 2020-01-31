from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
path('post/',post_upload,name='post_upload'),

]