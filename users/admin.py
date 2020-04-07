from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.Country)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("name",)

    list_filter = ("name",)


@admin.register(models.Department)
class CustomUserAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Organization", {"fields": ("name", "koica_code")},),
        ("Countries", {"fields": ("countries",)},),
    )

    list_display = (
        "name",
        "count_countries",
    )

    list_filter = (
        "name",
        "countries",
    )

    filter_horizontal = ("countries",)

    def count_countries(self, obj):
        return obj.countries.count()

    count_countries.short_description = "Country Count"


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
