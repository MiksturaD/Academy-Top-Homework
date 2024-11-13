from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from authors.models import Author, TopBooks
def index(request):
    authors = Author.objects.all()
    top_books = TopBooks.objects.all()
    return render(request, 'index.html', {
        'authors': authors,
        'top_books': top_books,
    })
def author(request, author_id):
    author = Author.objects.all()
    top_books = TopBooks.objects.filter(author_id=author_id)
    return render(request, 'detail.html', {
        'author': author,
        'top_books': top_books
    })

def top_book(request):
    top_books = TopBooks.objects.all()  # Получаем все топ-книги
    return render(request, 'top_book.html')

def detail(request, author_id=None, top_book_id=None):
    author = get_object_or_404(Author, pk=author_id)  # Получаем автора по ID
    top_book = TopBooks.objects.filter(author_id=author_id)  # Получаем топ-книгу по ID
    return render(request, 'detail.html',{'author':author, 'top_book':top_book})
