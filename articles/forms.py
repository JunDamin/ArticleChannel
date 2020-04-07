from django import forms
from django_countries.fields import CountryField
from . import models


class CreateArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = models.Article
        fields = (
           "country", "article_date", "title", "subject_type", "sector", "content", "article_source", "article_link",
        )
        widgets = {
            "article_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "title": forms.TextInput(attrs={"placeholder": "제목"}),
            "content": forms.Textarea(attrs={"placeholder": "내용"}),
            "article_source": forms.TextInput(attrs={"placeholder": "출처"}),
            "article_link": forms.TextInput(attrs={"placeholder": "링크"}),
        }

    def save(self, *args, **kwargs):
        article = super().save(commit=False)
        return article


class SearchForm(forms.Form):
    country = CountryField(default="KR").formfield()
