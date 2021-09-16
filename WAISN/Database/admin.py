from django.contrib import admin
from .models import Product
from .forms import CreateProductForm

# Improves upon the basic admin page functionality by
#   displaying the database as a formatted table


class CreateProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_quantity"]
    form = CreateProductForm


admin.site.register(Product, CreateProductAdmin)
