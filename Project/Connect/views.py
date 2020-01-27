from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    print(request.user)
    if request.user.is_authenticated:
      return render(request,'Front.html') 
    else:
      return redirect(adminLogin)

def register(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return HttpResponse('you are not an admin bro')
    if request.method =="GET":
        return render(request,'register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return render(request,'login.html')

def adminLogin(request): 
    if request.method =="GET":
        return render (request,'login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect(adminPanel)
        else:
            return HttpResponse("Authentication Failed")


def adminPanel(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return HttpResponse('you are not an admin bro')
    print(request.user)
    if request.user.is_authenticated:
      return render(request,'admin.html') 
    else:
      return redirect(adminLogin)

def adminLogout(request):
    logout(request)
    return redirect(adminLogin) 

def userLogin(request):
    if request.method=="GET":
        return render(request,'slogin.html') 
    else:
        print(request.Post) 
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponse("Logged in")
        else:
            return HttpResponse("Authentication Failed")

def userLogout(request):
    logout(request)
    return redirect(userLogin)    