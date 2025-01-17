from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  name = models.CharField(max_length=100, verbose_name='Название категории')

  def __str__(self):
    return self.name

class Product(models.Model):
  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
  name = models.CharField(max_length=100, verbose_name='Название')
  description = models.TextField(verbose_name='Описание')
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
  is_available = models.BooleanField(default=True, verbose_name='Доступен ли к заказу')
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

  def __str__(self):
    return f'{self.name}, {self.description}, {self.price}, {self.is_available}, {self.category}'

class Order(models.Model):
  class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'
  customer_name = models.CharField(max_length=100, verbose_name='Имя покупателя')
  customer_email = models.EmailField(verbose_name='Емайл')
  order_date = models.DateTimeField(verbose_name='Дата заказа')
  line = models.ManyToManyField(Product)


  def __str__(self):
    return f'{self.customer_name}, {self.order_date}, {self.line}'


class User(AbstractUser):
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
  first_name = models.CharField(max_length=100, verbose_name='Имя')
  last_name = models.CharField(max_length=100, verbose_name='Фамилия')

  def __str__(self):
    return self.username