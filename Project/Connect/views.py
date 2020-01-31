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
          return render(request,'Front.html') 
    else:
      return redirect(Login)

def register(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return HttpResponse('you are not an admin bro')
    if request.method =="GET":
        return render(request,'register.html')
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, password=password, username="")
        if request.POST.get('is_staff'):
            user.is_staff = True
        else:
            user.is_staff = False  
        user.save()
        return redirect(Login)

def Login(request):
    if request.user.is_authenticated:
        return redirect(adminPanel)
    if request.method =="GET":
        return render (request,'login.html')
    else:
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user1 = authenticate(email=email,password=password)
        user2 = authenticate(username=username, password=password)
        if user1 is not None:
            login(request,user1)
            return redirect(adminPanel)
        elif user2 is not None:
            login(request,user2)
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

  