from django.contrib import admin

from .models import *

@admin.register(ObjectViewed)
class ObjectViewedAdmin(admin.ModelAdmin):


    class Meta:
        model = ObjectViewed
