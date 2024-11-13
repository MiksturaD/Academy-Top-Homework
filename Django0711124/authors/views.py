from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Author, TopBooks
def index(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'author':author})

def author(request, author_id=None):
    author = Author.objects.get(Author, pk=author_id)  # Получаем автора по ID
    return render(request, 'authors.html', {'author':author})

def top_book(request):
    top_books = TopBooks.objects.all()  # Получаем все топ-книги
    return render(request, 'top_book.html')

def detail(request, author_id=None, top_book_id=None):
    author = get_object_or_404(Author, pk=author_id)  # Получаем автора по ID
    top_book = get_object_or_404(TopBooks, pk=top_book_id)  # Получаем топ-книгу по ID
    return render(request, 'detail.html',{'author':author, 'top_book':top_book})
