
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse(f"Наш город красноярск!")


def news(request):
    return render(request, 'news.html')


def governance(request):
    return HttpResponse(f"Администрация города")


def facts(request):
    return HttpResponse(f"Факты о нашем городе")


def contact(request):
    return HttpResponse(f"Контактная страничка Красноярска")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)