
from django.contrib import admin

from store.models import Category, Product, Order, User

admin.site.site_header = "Интернет магазин по продаже HI-FI техники"
admin.site.site_title = "Админка магазина"
admin.site.index_title = "Добро пожаловать в магазин"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_available', 'category')
    list_filter = ('name', 'description', 'price', 'is_available', 'category')  # Фильтры в правой части админки
    search_fields = ('name', )  # Поля для поиска

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'order_date')
    list_filter = ('customer_name', 'order_date')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')



