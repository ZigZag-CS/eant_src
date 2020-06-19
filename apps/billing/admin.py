from django.contrib import admin

from .models import *

@admin.register(BillingProfile)
class OrderAdmin(admin.ModelAdmin):


    class Meta:
        model = BillingProfile
