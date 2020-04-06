from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.

class Article(core_models.TimeStampedModel):
    author = models.ForeignKey('users.User', related_name='article', on_delete=models.CASCADE)
    country = CountryField()
    article_date = models.DateField()
    title = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=16)
    article_field = models.CharField(max_length=16)
    content = models.TextField()
    article_source = models.CharField(max_length=255)
    article_link = models.TextField()