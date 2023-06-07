from django.urls import path
from . import views
from .views import BoardView

urlpatterns = [
    path("board/", BoardView.as_view(), name="board")
]