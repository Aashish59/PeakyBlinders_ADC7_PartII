from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('changepassword/', change_password,name='auth_password_change'),
]