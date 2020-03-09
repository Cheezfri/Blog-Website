from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Alex',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 8th, 2020'
    },
    {
        'author': 'Alec',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 9th, 2020'
    }
]


def home(request):  # Views either return a http response or exception
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)  # http response is returned in background


def about(request):
    return render(request, 'blog/about.html')
