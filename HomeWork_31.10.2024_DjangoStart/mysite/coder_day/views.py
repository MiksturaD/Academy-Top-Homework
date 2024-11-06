
from django.http import HttpResponse
from django.shortcuts import render

def coder_day(request):
    return HttpResponse(f'Каждый год отмечают день программиста 256 день в году')
