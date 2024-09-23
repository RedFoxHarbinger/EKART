from django.contrib import admin
from . models import products

# Register your models here.
@admin.register(products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'display_size']
    list_filter = ['display_size']
    search_fields = ['title']