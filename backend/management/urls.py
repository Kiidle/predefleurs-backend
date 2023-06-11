from django.urls import path
from . import views
from .views import BoardView, CreateTaskView

urlpatterns = [
    path("board/", BoardView.as_view(), name="board"),
    path("board/tasks/create", CreateTaskView.as_view(), name="task_create"),
]