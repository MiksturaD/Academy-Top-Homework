from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  is_available = models.BooleanField(default=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}, {self.description}, {self.price}, {self.is_available}, {self.category}'

class Order(models.Model):
  customer_name = models.CharField(max_length=100)
  customer_email = models.EmailField()
  order_date = models.DateTimeField()
  line = models.ManyToManyField(Product)


  def __str__(self):
    return f'{self.customer_name}, {self.order_date}, {self.line}'