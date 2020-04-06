from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("author", "country", "article_date", "title", "subject_type", "article_field",)
            },
        ),
        (
            "Contents",
            {
                "fields": ("content", "article_source", "article_link",)
            },
        ),
    )

    list_display = ("author", "country", "article_date", "title", "subject_type", "article_field", "article_source", "article_link",
        
    )

    list_filter = (
        "subject_type",
        "article_field",
        "country",
    )

    raw_id_fields = ("author", )

    search_fields = ["country", "title", "article_source"]
