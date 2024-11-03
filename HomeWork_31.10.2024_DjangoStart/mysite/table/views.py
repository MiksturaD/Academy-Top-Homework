from django.http import HttpResponse
from django.shortcuts import render


def table(request):
    table = "<table border='1'>"
    for i in range(1, 10):
        table += "<tr>"
        for j in range(1, 10):
            table += f"<td>{i * j}</td>"
        table += "</tr>"
    table += "</table>"
    return HttpResponse(f"Таблица умножения<br>{table}")