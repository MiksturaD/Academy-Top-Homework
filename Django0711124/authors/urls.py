from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('author/<int:author_id>/', views.author, name='author'),
    path('top_book/<int:top_book_id>', views.top_book, name="top_book"),
    path('detail/<int:author_id>/<int:top_book_id>/', views.detail, name="detail"),
]