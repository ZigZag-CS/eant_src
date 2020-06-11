from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product
