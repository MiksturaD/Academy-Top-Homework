from django.contrib import admin

from store.models import Category, Product, Order, User

admin.site.site_header = "Интернет магазин по продаже HI-FI техники"
admin.site.site_title = "Админка магазина"
admin.site.index_title = "Добро пожаловать в магазин"

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)



