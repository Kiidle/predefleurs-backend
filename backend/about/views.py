from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from about.models import Opening, About

User = get_user_model()


# Create your views here.

class AboutView(generic.ListView):
    model = About
    fields = ['number', 'title', 'description']
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["abouts"] = super().get_queryset()

        return context


class CreateAboutView(generic.CreateView):
    model = About
    fields = ['number', 'title', 'image', 'description']
    template_name = "pages/form_about.html"

    def get_success_url(self):
        return reverse_lazy('about')

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateAboutView(generic.UpdateView):
    model = About
    fields = ['number', 'title', 'image', 'description']
    template_name = "pages/form_about.html"

    def get_success_url(self):
        return reverse_lazy('about')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteAboutView(generic.DetailView):
    model = About
    fields = ['number', 'title', 'image', 'description']
    template_name = "pages/delete_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def delete_about(request, pk):
    about = About.objects.get(pk=pk)

    if request.method == "POST":
        about.delete()
        return redirect("about")

    return (request, "/about", {"about": about})


class OpeningView(generic.ListView):
    model = Opening
    fields = ['day', 'time_morning_from', 'time_morning_to', 'time_afternoon_from', 'time_afternoon_to']
    template_name = "pages/opening.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["openings"] = self.get_queryset()
        return context

class UpdateOpeningView(generic.UpdateView):
    model = Opening
    fields = ['time_morning_from', 'time_morning_to', 'time_afternoon_from', 'time_afternoon_to']
    template_name = "pages/form_opening.html"

    def get_success_url(self):
        return reverse_lazy('opening')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
