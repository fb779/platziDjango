from django.contrib import admin
from .models import (Category, Product, ImageProduct)
from .forms import (ProductAdminForm, ProductForm)
# Register your models here.


# @admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('ct_name', 'ct_description',)
#   list_filter = ()


@admin.register(ImageProduct)
class AdminImage(admin.ModelAdmin):
    list_display = ('producto', 'image',)


# @admin.register(Product)
# class AdminProduct(admin.ModelAdmin):
#     list_display = ('name', 'description', 'category', 'image',)
#     #   list_filter = ()

@admin.register(Product)
class AdminProductForm(admin.ModelAdmin):
    list_display = ('description', 'name', 'category', 'image',)
    form = ProductForm
    # form = ProductAdminForm

# Registra un modelo con un formulario "admin.site.register(Model, Form)"
# admin.site.register(Product, ProductForm)