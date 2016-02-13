from django.contrib import admin
from .models import (Category, Product)
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('ct_name', 'ct_description',)
    #list_filter = ()
    
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('pr_name', 'pr_description', 'pr_image', 'pr_category',)
    #list_filter = ()
