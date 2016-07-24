from django.contrib import admin
from .models import (Category, Product, ImageProduct)
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('ct_name', 'ct_description',)
#   list_filter = ()


@admin.register(ImageProduct)
class AdminImage(admin.ModelAdmin):
    list_display = ('producto', 'image',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'image',)
#   list_filter = ()
