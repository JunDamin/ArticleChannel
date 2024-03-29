from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


# Create your models here. de(self):
    # TODO: write code...


class Article(core_models.TimeStampedModel):

    SUBJECT_TYPE_CHOICES = (
        ("rc", "수원국"),
        ("dn", "공여국"),
        ("in", "국제기구"),
        ("ko", "KOICA"),
    )
    SECTOR_CHOICES = (
        ("edu", "교육"),
        ("hea", "보건의료"),
        ("gov", "공공행정"),
        ("agr", "농림수산"),
        ("tec", "기술환경에너지"),
        ("emr", "긴급구호"),
        ("etc", "기타"),
    )

    author = models.ForeignKey(
        "users.User", related_name="article", on_delete=models.CASCADE
    )
    country = CountryField()
    article_date = models.DateField()
    title = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=16, choices=SUBJECT_TYPE_CHOICES)
    sector = models.CharField(max_length=16, choices=SECTOR_CHOICES)
    content = models.TextField()
    article_source = models.CharField(max_length=255, blank=True)
    article_link = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"pk": self.pk})
