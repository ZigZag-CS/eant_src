from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class OrderAdmin(admin.ModelAdmin):


    class Meta:
        model = Cart