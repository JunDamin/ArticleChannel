from django import forms
from django_countries.fields import CountryField
from . import models
from users import models as user_models


class CreateArticleForm(forms.ModelForm):

    country = forms.ChoiceField(required=True)

    class Meta:
        model = models.Article
        fields = (
            "country",
            "article_date",
            "title",
            "subject_type",
            "sector",
            "content",
            "article_source",
            "article_link",
        )
        widgets = {
            "article_date": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"}),
            "title": forms.TextInput(attrs={"placeholder": "제목"}),
            "content": forms.Textarea(attrs={"placeholder": "내용"}),
            "article_source": forms.TextInput(attrs={"placeholder": "출처"}),
            "article_link": forms.TextInput(attrs={"placeholder": "링크"}),
        }

    def __init__(self, user, *args, **kwargs):
        # 인자를 받기 위해서는 view에서 get_from_kwargs를 정의하고 super를 통해서 user 값을 확보해야 한다.
        super(CreateArticleForm, self).__init__(*args, **kwargs)
        self.fields["country"].choices = (
            (i.name, i) for i in user.department.countries.all()
        )

    def save(self, *args, **kwargs):
        article = super().save(commit=False)
        return article


class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = (
            "country",
            "title",
            "subject_type",
            "sector",
        )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
