# mysite/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post1

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

def index1(request):
    return render(request, 'index1.html', {
        'current_time': str(datetime.now()),
    })

def post_list1(request):
    posts = Post1.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def hello_world1(request):
    return render(request, 'hello_world1.html', {
        'current_time': str(datetime.now()),
    })    
"""def hello_world(request):
    return HttpResponse("Hello World!")
"""