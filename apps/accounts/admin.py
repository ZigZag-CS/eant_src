from django.contrib import admin

from .models import GuestEmail

@admin.register(GuestEmail)
class GuestEmailAdmin(admin.ModelAdmin):

    class Meta:
        model = GuestEmail
