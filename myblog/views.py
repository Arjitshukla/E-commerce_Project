# Create your views here.
from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def blogpage(request):
    myposts= Blogpost.objects.all()
    return render(request, 'blog.html', {'myposts': myposts})
    # return render(request, 'blog.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',
                  {'post':post})
