from django.contrib import admin
from import_export.admin import ImportExportMixin
from . import models

# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("author", "country", "article_date", "title", "subject_type", "sector",)
            },
        ),
        (
            "Contents",
            {
                "fields": ("content", "article_source", "article_link",)
            },
        ),
    )

    list_display = ("author", "country", "article_date", "title", "subject_type", "sector", "article_source", "article_link",
        
    )

    list_filter = (
        "subject_type",
        "sector",
        "country",
    )

    raw_id_fields = ("author", )

    search_fields = ["country", "title", "article_source"]
