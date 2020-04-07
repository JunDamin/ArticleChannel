from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from . import models, forms

# Create your views here.

class HomeView(ListView):
    model = models.Article
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "articles"

class CreateArticleView(FormView):
    
    form_class = forms.CreateArticleForm
    template_name = "articles/article_create.html"
    
    def form_valid(self, form):
        article = form.save()
        article.author = self.request.user
        article.save()
        return redirect(reverse("article:detail", kwargs={"pk": article.pk}))


class ArticleDetail(DetailView):

    """ ArticleDetail Definition """

    model = models.Article


class EditArticleView(UpdateView):

    model = models.Article
    template_name = "articles/article_edit.html"
    fields = (
           "country", "article_date", "title", "subject_type", "sector", "content", "article_source", "article_link",
        )

    def get_object(self, queryset=None):
        article = super().get_object(queryset=queryset)
        if article.author.pk != self.request.user.pk:
            raise Http404()

        return article

@login_required
def delete_article(request, pk):
    user = request.user
    try:
        article = models.Article.objects.get(pk=pk)
        if article.author.pk != user.pk:
            messages.error(request, "Can't delete that article")
        else:
            models.Article.objects.filter(pk=pk).delete()
            messages.success(request, "Article Deleted")
        return redirect((reverse("core:home")))
    except models.Article.DoesNotExist:
        return redirect((reverse("core:home")))

class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                subject_type = form.cleaned_data.get("subject_type")
                sector = form.cleaned_data.get("sector")

                filter_args = {}

                filter_args["country"] = country

                if subject_type is not None:
                    filter_args["subject_type"] = subject_type

                if sector is not None:
                    filter_args["sector"] = sector

                qs = models.Article.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                articles = paginator.get_page(page)

                return render(
                    request, "article/search.html", {"form": form, "articles": articles}
                )

        else:

            form = forms.SearchForm()

            return render(request, "articles/search.html", {"form": form})