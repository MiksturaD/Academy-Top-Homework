from itertools import product

from django.shortcuts import render

from store.models import Category, Product


# Create your views here.
def index(request):
  category_list = Category.objects.all()
  return render(request, 'store/index.html', context={'categories': category_list, 'category_id': id})

def categories(request):
  category_list = Category.objects.all()
  return render(request, 'store/categories.html', context={'categories': category_list, 'category_id': id})

def category(request):
  category = get_object_or_404(Category, id=category_id)
  product_list = Product.objects.all()
  return render(request, 'store/category.html', context={'category': category, 'products': product_list})


def products(request):
  product_list = Product.objects.all()
  category_list = Category.objects.all()
  return render(request, 'store/products.html', context={'category': category_list, 'category_id': id,
                                                         'products': product_list})


def orders(request):
  return render(request, 'store/orders.html')


def order(request):
  return None