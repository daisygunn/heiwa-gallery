from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Category admin management """
    list_display = ("category_name", "name_to_display")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin management """
    list_display = ("pk", "name", "category", "photographer_artist", "size",
                    "quantity_in_stock", "price", "image",
                    "in_stock", "date_added", "category_id")
