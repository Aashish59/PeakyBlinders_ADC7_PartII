from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.template import loader
from .models import *
# Create your views here.
def post_upload(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    elif request.method == 'POST':
        post = Post.objects.create(content=request.POST['content'],
                                     created_at=datetime.utcnow())
        post.save()
        return HttpResponseRedirect(reverse('post_details', kwargs={'post_id': post.id}))

       
