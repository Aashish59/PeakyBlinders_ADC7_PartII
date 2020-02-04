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
    if request.method == 'GET':
        return HttpResponse(loader.get_template('upload.html').render({},request))
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(content=content, title=title)
        post.save()
        return redirect(home)


