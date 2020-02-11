from django.shortcuts import render
from Post.models import Post
from django.http import HttpResponse
from django.db.models import Q 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def search(request):
    post=Post.objects.all()
    query=request.GET.get('srh')
    if query:
        posts=Post.objects.filter(Q(title__icontains=query)) 
        if posts:
            return render(request,'search.html', {
                    'posts': posts
                })
        else:
                return render(request,'search.html', {
                    'posts': posts
                })
    
    return render(request,'base.html',{
        'post': post
    })    
            
