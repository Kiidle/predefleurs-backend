from django.urls import path
from . import views
from .views import ArticlesView

urlpatterns = [
    path("", ArticlesView.as_view(), name="articles")
]