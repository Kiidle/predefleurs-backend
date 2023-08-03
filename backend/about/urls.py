from django.urls import path
from . import views
from .views import AboutView, CreateAboutView, UpdateAboutView, DeleteAboutView, OpeningView, UpdateOpeningView

urlpatterns = [
    path("", AboutView.as_view(), name="about"),
    path("/create", CreateAboutView.as_view(), name="about_create"),
    path("about-<int:pk>/update", UpdateAboutView.as_view(), name="about_update"),
    path("about-<int:pk>/delete", DeleteAboutView.as_view(), name="about_delete"),
    path("about-<int:pk>/delete-confirmed", views.delete_about, name="about_delete_confirmed"),
    path("opening", OpeningView.as_view(), name="opening"),
    path("opening-<int:pk>/update", UpdateOpeningView.as_view(), name="opening_update"),
]