from django.shortcuts import render
from .models import Post  # Since model is in same directory, use '.'
# from django.http import HttpResponse


def home(request):  # Views either return a http response or exception
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)  # http response is returned in background


def about(request):
    return render(request, 'blog/about.html')
