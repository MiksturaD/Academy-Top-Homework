from django.contrib import admin

from store.models import Category, Product, Order, User

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)



