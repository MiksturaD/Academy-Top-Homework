from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="main"),
    path('writers/<int:author_id>/', views.writers, name='writers'),
    path('books/', views.books, name='books'),
    path('detail/<int:author_id>/<int:top_book_id>/', views.detail, name="detail"),
]