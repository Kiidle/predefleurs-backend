from django.urls import path
from . import views
from .views import BoardView, CreateTaskView, TaskView, UpdateTaskView, AssignTaskView, StatusTaskView

urlpatterns = [
    path("board/", BoardView.as_view(), name="board"),
    path("tasks/create", CreateTaskView.as_view(), name="task_create"),
    path("tasks/<int:pk>", TaskView.as_view(), name="task"),
    path("tasks/<int:pk>/update", UpdateTaskView.as_view(), name="task_update"),
    path("tasks/<int:pk>/assign", AssignTaskView.as_view(), name="task_assign"),
    path("tasks/<int:pk>/status", StatusTaskView.as_view(), name="task_status"),
]