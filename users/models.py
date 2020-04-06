from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db import models

# Create your models here.

class User(AbstractUser):

    
    
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    bio = models.TextField(default="", blank=True)

    office = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=64, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )


    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        
        return