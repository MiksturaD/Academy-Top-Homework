from django.urls import path

from store import views


urlpatterns = [
    path('', views.index, name='index'),

    path('category/<int:category_id>/', views.category, name='category'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('category/<int:category_id>/<int:product_id>', views.product, name='categories'),
    path('category/create/', views.create_category, name='create_category'),
    path('order/create/', views.create_order, name='create_order'),
    path('products', views.products, name='products'),
    path('products/create/', views.create_product, name='create_product'),
    path('orders', views.orders, name='orders'),
    path('orders/<int:order_id>', views.order, name='order'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
