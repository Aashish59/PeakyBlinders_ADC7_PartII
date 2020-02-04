from django.contrib import admin
from django.urls import path
from Post.views import post_upload

urlpatterns = [
    path('uploads/', post_upload)
]