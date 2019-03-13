from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'THavart',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'March 11, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'March 12, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
