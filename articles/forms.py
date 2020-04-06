from django import forms
from . import models


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = (
           "country", "article_date", "title", "subject_type", "article_field", "content", "article_source", "article_link",
        )

    def save(self, *args, **kwargs):
        article = super().save(commit=False)
        return article