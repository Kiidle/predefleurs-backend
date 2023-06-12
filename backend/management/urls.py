from django.urls import path
from . import views
from .views import BoardView, CreateTaskView, TaskView

urlpatterns = [
    path("board/", BoardView.as_view(), name="board"),
    path("tasks/create", CreateTaskView.as_view(), name="task_create"),
    path("tasks/<int:pk>", TaskView.as_view(), name="task"),
]