from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def author(request):
    return render(request, 'author.html')

def top_book(request):
    return render(request, 'top_book.html')