from django.urls import path

from store import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('products', views.products, name='products'),
    path('orders', views.orders, name='orders'),
    path('orders/<int:order_id>', views.order, name='order'),
]
