from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.template import loader

from Post.models import Post

# Create your views here.
def home(request):
    if request.user.is_superuser and request.user.is_staff:
        return redirect(adminPanel)
    if request.user.is_authenticated:
            queryset = Post.objects.all()
            context={
            "object_list": queryset
        }
            return HttpResponse(loader.get_template('authenticatedHome.html').render(context,request))
        
    else:
      return HttpResponse(loader.get_template('home.html').render({},request))

def accounts(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect(home)
    else:
        if request.user.is_authenticated:
            queryset = User.objects.all()
            context={
                "object_list": queryset
            }
            return HttpResponse(loader.get_template('accounts.html').render(context,request))
        else:
            return HttpResponse(loader.get_template('home.html').render({},request))
            
def register(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect(home)
    if request.method =="GET":
        return HttpResponse(loader.get_template('register.html').render({},request))
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse(loader.get_template("register.html").render({
            "messages" : [
                {
                    "type" : "danger",
                    "content" : "Username is already taken"
                }
            ],
        }, request))
        elif User.objects.filter(email=email).exists():
            return HttpResponse(loader.get_template("register.html").render({
            "messages" : [
                {
                    "type" : "danger",
                    "content" : "Email is already taken"
                }
            ],
        }, request))
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username, email=email, password=password)
            if request.POST.get('is_staff'):
                user.is_staff = True
            else:
                user.is_staff = False  
            user.save()
            return redirect(accounts)  

def delete(request, id):  
    users = User.objects.get(id=id)  
    users.delete()  
    return redirect(accounts) 

def Login(request):
    if request.user.is_authenticated:
        return redirect(adminPanel)
    if request.method =="GET":
        return HttpResponse(loader.get_template('login.html').render({},request))
    else:
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(adminPanel)
        else:
            return HttpResponse(loader.get_template("login.html").render({
            "messages" : [
                {
                    "type" : "danger",
                    "content" : "Incorrect username or password "
                }
            ],
        }, request))   

def adminPanel(request):
    if request.user.is_superuser and request.user.is_staff:
        queryset = Post.objects.all()
        context={
            "object_list": queryset
            }
        return HttpResponse(loader.get_template('admin.html').render(context,request))
        
    if request.user.is_authenticated:
       return redirect(home)
    else:
      return redirect(Login)
    
def Logout(request):
    logout(request)
    return redirect(home) 



  