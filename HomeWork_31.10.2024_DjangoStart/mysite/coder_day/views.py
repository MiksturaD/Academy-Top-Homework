from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    now = datetime.()
    return HttpResponse(f"Текущая дата и время: {now}")
