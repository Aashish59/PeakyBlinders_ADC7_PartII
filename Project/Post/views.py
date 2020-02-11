from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.template import loader
from Connect.views import home
from Post.models import Post

from Connect.views import home


# Create your views here.
def post_upload(request):
    if not request.user.is_authenticated:
        return redirect(home)
    if request.method == 'GET':
        return HttpResponse(loader.get_template('upload.html').render({},request))
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        files = request.POST.get('files')
        post = Post.objects.create(content=content, title=title, files=files)
        post.user = request.user
        post.save()
        return redirect(home)

def post_delete(request,id):  
    post = Post.objects.get(id=id)  
    post.delete()  
    return redirect(home)

def post_edit(request,id): 
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit.html', {'post': post} )
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.files = request.POST['files']
        post.save()
        return redirect(home)    
     
