from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.dispatch import receiver
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import Group

from django.db.models.signals import post_save

from django.contrib.auth import authenticate, get_user_model, login, logout

from store.models import Article, Reservation

User = get_user_model()


# Create your views here.

class ArticlesView(generic.ListView):
    model = Article
    fields = ['title', 'description', 'author']
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


class ReservationView(generic.ListView):
    model = Reservation
    fields = ['article', 'start_date', 'status']
    template_name = "pages/reservation/reservations.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        queryset = queryset.filter(Q(status=Reservation.Status.OPEN) | Q(status=Reservation.Status.APPROVED) | Q(status=Reservation.Status.READY))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = self.get_queryset()
        return context


class ArchivedReservationView(generic.ListView):
    model = Reservation
    fields = ['article', 'start_date', 'status']
    template_name = "pages/reservation/archive.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        queryset = queryset.filter(Q(status=Reservation.Status.DENIED) | Q(status=Reservation.Status.DONE))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = self.get_queryset()
        return context


def create_reservation(request, article_id):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, id=article_id)
        Reservation.objects.create(article=article, user=request.user, status=Reservation.Status.OPEN)
        return redirect('reservations')
    else:
        return redirect('login')
