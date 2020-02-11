from django.contrib import admin
from django.urls import path
from Post.views import post_upload,post_delete,post_edit

urlpatterns = [
    path('uploads/',post_upload),
    path('deletepost/<int:id>',post_delete),
    path('editpost/<int:id>',post_edit),
]