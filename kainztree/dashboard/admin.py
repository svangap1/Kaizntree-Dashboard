from django.contrib import admin
from .models import Category, Item
# Register your models here.
class CategoryRef(admin.ModelAdmin):
    list_display = ['id','name']

class ItemRef(admin.ModelAdmin):
    list_display = ['sku','name']
    
admin.site.register(Category, CategoryRef)
admin.site.register(Item, ItemRef)