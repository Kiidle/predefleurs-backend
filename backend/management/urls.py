from django.urls import path
from . import views
from .views import BoardView, CreateTaskView, TaskView, UpdateTaskView, AssignTaskView, StatusTaskView, DeleteTaskView, ManageReservationsView, ManageReservationsArchivedView, UpdateReservation

urlpatterns = [
    path("board/", BoardView.as_view(), name="board"),
    path("tasks/create", CreateTaskView.as_view(), name="task_create"),
    path("tasks/<int:pk>", TaskView.as_view(), name="task"),
    path("tasks/<int:pk>/update", UpdateTaskView.as_view(), name="task_update"),
    path("tasks/<int:pk>/assign", AssignTaskView.as_view(), name="task_assign"),
    path("tasks/<int:pk>/status", StatusTaskView.as_view(), name="task_status"),
    path("tasks/<int:pk>/delete", DeleteTaskView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/delete-confirmed", views.delete_task, name="task_delete_confirmed"),
    path("reservations", ManageReservationsView.as_view(), name="manage_reservations"),
    path("reservations/archived", ManageReservationsArchivedView.as_view(), name="manage_reservations_archived"),
    path("reservations/<int:pk>/update", UpdateReservation.as_view(), name="manage_reservations_update"),
]