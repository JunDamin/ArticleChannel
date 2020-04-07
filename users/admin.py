from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.Department)
class CustomUserAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Organization", {"fields": ("name", "koica_code")},),
        ("Countries", {"fields": ("workon_countries",)},),
    )
    list_filter = (
        "name",
        "workon_countries",
    )

    list_display = (
        "name",
        "workon_countries",
    )


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    fieldsets = (("Organization", {"fields": ("department",)},),) + UserAdmin.fieldsets

    list_filter = UserAdmin.list_filter + ("department",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "department",
    )
