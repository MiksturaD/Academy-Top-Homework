from itertools import product

from django.shortcuts import render, get_object_or_404, redirect
from store.forms import CategoryCreateForm, OrderCreateForm
from store.models import Category, Product, Order


# Create your views here.
def index(request):
  category_list = Category.objects.all()
  return render(request, 'store/index.html', context={'categories': category_list})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product_list = Product.objects.filter(category=category)
    return render(request, 'store/category/list.html', context={'category': category,
                                                                'products': product_list})


def products(request):
  product_list = Product.objects.all()
  category_list = Category.objects.all()
  return render(request, 'store/product/products.html', context={'category': category_list,
                                                                 'category_id': id,'products': product_list})


def orders(request):
    orders_list = Order.objects.all()
    return render(request, 'store/order/list.html', context={'orders': orders_list})


def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = sum(product.price for product in order.line.all())
    return render(request, 'store/order/detail.html', context={'order': order, 'total_price': total_price})

def create_category(request):
  if request.method == 'POST':
       form = CategoryCreateForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('category')
  else:
    form = CategoryCreateForm()

  return render(request, 'store/category/create.html', {'form': form})

def create_order(request):
  if request.method == 'POST':
       form = OrderCreateForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('order')
  else:
    form = OrderCreateForm()

  return render(request, 'store/order/create.html', {'form': form})