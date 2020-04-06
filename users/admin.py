from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    
    fieldsets = (("Organization",{"fields": ("office",) },),) + UserAdmin.fieldsets

    list_filter = UserAdmin.list_filter + ("office",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "office",)