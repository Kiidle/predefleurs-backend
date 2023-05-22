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