from django.contrib import admin

from .models import LoyaltyUser


@admin.register(LoyaltyUser)
class LoyaltyUserAdmin(admin.ModelAdmin):
    pass
