from django.contrib import admin

from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):


    class Meta:
        model = Order
