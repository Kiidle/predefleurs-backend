from django.urls import path
from . import views
from .views import ArticlesView, CreateArticleView, UpdateArticleView, DeleteArticleView, ReservationView, ArchivedReservationView

urlpatterns = [
    path("", ArticlesView.as_view(), name="articles"),
    path("create", CreateArticleView.as_view(), name="article_create"),
    path("article-<int:pk>/update", UpdateArticleView.as_view(), name="article_update"),
    path("article-<int:pk>/delete", DeleteArticleView.as_view(), name="article_delete"),
    path("article-<int:pk>/delete-confirmed", views.delete_article, name="article_delete_confirmed"),
    path('article-<int:article_id>/reservating/', views.create_reservation, name='create_reservation'),
    path("reservations/", ReservationView.as_view(), name="reservations"),
    path("reservations/archive", ArchivedReservationView.as_view(), name="archived_reservations")
]
