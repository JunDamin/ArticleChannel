from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

@admin.register(models.Department)
class CustomUserAdmin(admin.ModelAdmin):
    
    fieldsets = (("Organization",{"fields": ("namme",) },),)
    list_filter =  ("name",)

    list_display = (
        "name",)


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    
    fieldsets = (("Organization",{"fields": ("department",) },),) + UserAdmin.fieldsets

    list_filter = UserAdmin.list_filter + ("department",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "department",)