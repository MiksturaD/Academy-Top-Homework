
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def authors(request):
    return render(request, 'authors.html', {'home_url': '/authors'})


def top_books(request):
    return render(request, 'top_books.html',{'home_url': '/authors'})

