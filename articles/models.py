from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here.

class Article(core_models.TimeStampedModel):


    ARTICLE_FIELD_CHOICES = (("r", "수원국"), ("d", "공여국"), ("i", "국제기구"), ("k", "KOICA"))
    SUBJECT_TYPE_CHOICES = (("edu", "교육"), ("hea", "보건의료"), ("gov", "공공행정"), ("agr", "농림수산"), ("tec", "기술환경에너지"), ("emr", "긴급구호"), ("etc", "기타"))

    author = models.ForeignKey('users.User', related_name='article', on_delete=models.CASCADE)
    country = CountryField()
    article_date = models.DateField()
    title = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=16, choices=SUBJECT_TYPE_CHOICES)
    article_field = models.CharField(max_length=16, choices=ARTICLE_FIELD_CHOICES)
    content = models.TextField()
    article_source = models.CharField(max_length=255, blank=True)
    article_link = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"pk": self.pk})