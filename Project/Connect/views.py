from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method =="GET":
        return render(request,'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")

def ulogin(request):
    if request.method =="GET":
        return render (request,'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"page.html")
        else:
            return HttpResponse("Authentication Failed")  
