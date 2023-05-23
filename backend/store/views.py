from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import Group

from django.db.models.signals import post_save

from django.contrib.auth import authenticate, get_user_model, login, logout

from store.models import Article

User = get_user_model()


# Create your views here.

class ArticlesView(generic.ListView):
    model = Article
    fields = ['titlte', 'description', 'author']
    template_name = "pages/product/articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["articles"] = super().get_queryset()

        return context


class CreateArticleView(generic.CreateView):
    model = Article
    fields = ['title', 'image', 'description']
    template_name = "pages/product/form_article.html"

    def get_success_url(self):
        return reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class UpdateArticleView(generic.UpdateView):
    model = Article
    fields = ['title', 'image', 'description']
    template_name = "pages/product/form_article.html"

    def get_success_url(self):
        return reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteArticleView(generic.DetailView):
    model = Article
    fields = ['title', 'image', 'description']
    template_name = "pages/product/delete_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_article(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        article.delete()
        return redirect("articles")

    return (request, "/shop", {"article": article})
