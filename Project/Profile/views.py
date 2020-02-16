from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.shortcuts import loader
from django.shortcuts import redirect
from Connect.views import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def change_password(request):
    if request.method =="GET":
        return HttpResponse(loader.get_template('change-password.html').render({},request))
    else:
        oldpassword= request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        print(request.POST)
        if User.objects.filter(password=oldpassword).exists():
            if User.objects.filter(newpassword=confirmpassword):
                    user = User.objects.get(request.user.username)
                    user.set_password=newpassword
                    user.save()
                    return redirect(Logout)
        else:
             return HttpResponse(loader.get_template("change-password.html").render({
            "messages" : [
                {
                    "type" : "danger",
                    "content" : "Password not correct"
                }
            ],
        }, request))
              
