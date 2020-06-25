from django.contrib import admin

from .models import *

@admin.register(BillingProfile)
class OrderAdmin(admin.ModelAdmin):


    class Meta:
        model = BillingProfile


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):


    class Meta:
        model = Card

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):


    class Meta:
        model = Charge
