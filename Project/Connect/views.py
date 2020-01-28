from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.template import loader


# Create your views here.
def homepage(request):
    print(request.user)
    if request.user.is_authenticated:
      return render(request,'Front.html') 
    else:
      return redirect(Login)

def home(request):
    print(request.user)
    if request.user.is_authenticated:
      return HttpResponse('Welcome') 
    else:
      return redirect(Login)

def register(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return HttpResponse('you are not an admin bro')
    if request.method =="GET":
        return render(request,'register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        if request.POST.get('is_staff'):
            user.is_staff = True
        else:
            user.is_staff = False  
        user.save()
        return redirect(Login)

def Login(request):
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
            return HttpResponse(loader.get_template("login.html").render({
            "messages" : [
                {
                    "type" : "danger",
                    "content" : "Incorrect username and password "
                }
            ],
        }, request))


def adminPanel(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect(homepage)
    if request.user.is_staff and not request.user.is_superuser:
        return redirect(home)
    print(request.user)
    if request.user.is_authenticated:
      return render(request,'admin.html') 
    else:
      return redirect(Login)
    
def adminLogout(request):
    logout(request)
    return redirect(Login) 

  