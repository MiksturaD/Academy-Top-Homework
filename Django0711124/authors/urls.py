from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('authors', views.author, name='authors'),
    path('top_book', views.top_book, name="top_book"),
]