from itertools import product

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from store.forms import CategoryCreateForm, OrderCreateForm, ProductCreateForm, SignupForm, CustomUserChangeForm
from store.models import Category, Product, Order, User


# Create your views here.
def index(request):
  category_list = Category.objects.all()
  return render(request, 'store/index.html', context={'categories': category_list})

@login_required
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product_list = Product.objects.filter(category=category)
    return render(request, 'store/category/detail.html', context={'category': category,
                                                                'products': product_list})

@login_required
def products(request):
  product_list = Product.objects.all()
  category_list = Category.objects.all()
  return render(request, 'store/product/list.html', context={'category': category_list,
                                                                 'category_id': id,'products': product_list})
@login_required
def product(request, category_id):
  product_list = Product.objects.all()
  category = get_object_or_404(Category, id=category_id)
  return render(request, 'store/category/detail.html', context={'category': category,
                                                                 'category_id': id,'products': product_list})

@login_required
def orders(request):
    orders_list = Order.objects.all()
    return render(request, 'store/order/list.html', context={'orders': orders_list})

@login_required
def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = sum(product.price for product in order.line.all())
    return render(request, 'store/order/detail.html', context={'order': order, 'total_price': total_price})

@login_required
def create_category(request):
  if request.method == 'POST':
       form = CategoryCreateForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('index')
  else:
    form = CategoryCreateForm()

  return render(request, 'store/category/create.html', {'form': form})

@login_required
def create_order(request):
  if request.method == 'POST':
       form = OrderCreateForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('orders')
  else:
    form = OrderCreateForm()

  return render(request, 'store/order/create.html', {'form': form})

@login_required
def create_product(request):
  if request.method == 'POST':
       form = ProductCreateForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('products')
  else:
    form = ProductCreateForm()

  return render(request, 'store/product/create.html', {'form': form})

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
      user.save()
      return redirect('signin')
  else:
    form = SignupForm()
  return render(request, 'auth/signup.html', {'form': form})


def signin(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    # Аутентификация пользователя
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)  # Вход пользователя
      return redirect('main')  # Перенаправление после успешного входа
    else:
      # Ошибка входа
      return render(request, 'auth/signin.html', {'error': 'Неверный логин или пароль'})
  return render(request, 'auth/signin.html')


def signout(request):
  # Выходим из системы
  logout(request)
  # Перенаправляем пользователя на страницу входа
  return redirect('signin')


@login_required
def main(request):
  return render(request, 'store/main.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление на страницу профиля после успешного сохранения
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'store/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'store/profile.html')