from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import title

from authors.models import Author, TopBooks

def writers(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'writers.html', {'author': author})

def detail(request, author_id, top_book_id):
    author = get_object_or_404(Author, id=author_id)  # Получаем автора по ID
    top_book = get_object_or_404(TopBooks, id=top_book_id, author=author)  # Получаем конкретную топ-книгу по ID и
                                                                            # проверяем, принадлежит ли она автору

    return render(request, 'detail.html', {
        'author': author,
        'top_book': top_book,
    })


def books(request, top_books_id=None):
    if top_books_id is not None:
        top_books = get_object_or_404(TopBooks, id=top_books_id)
        author = top_books.author
    else:
        top_books = TopBooks.objects.all()
        author = None
    return render(request, 'books.html', {'author': author, 'top_books': top_books})