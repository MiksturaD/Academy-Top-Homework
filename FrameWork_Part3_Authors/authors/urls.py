from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('authors', views.authors, name='news'),
    path('top_books', views.top_books, name="governance"),
]