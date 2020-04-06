from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [path("create/", views.CreateArticleView.as_view(), name="create"),
    path("<int:pk>", views.ArticleDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditArticleView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_article, name="delete", ),]