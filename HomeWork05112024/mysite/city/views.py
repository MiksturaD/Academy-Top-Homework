
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def news(request):
    return render(request, 'news.html', {'home_url': '/city'})


def governance(request):
    return render(request, 'governance.html',{'home_url': '/city'})


def facts(request):
    return render(request, 'facts.html',{'home_url': '/city'})


def contact(request):
    return render(request, 'contact.html',{'home_url': '/city'})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)