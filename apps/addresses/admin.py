from django.contrib import admin

from .models import *

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):


    class Meta:
        model: Address
