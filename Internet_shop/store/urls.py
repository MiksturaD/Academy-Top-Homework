from django.urls import path

from store import views


urlpatterns = [
    path('', views.index, name='index'),

    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('category/<int:category_id>/<int:product_id>', views.product, name='categories'),
    path('products', views.products, name='products'),
    path('orders', views.orders, name='orders'),
    path('orders/<int:order_id>', views.order, name='order'),
]