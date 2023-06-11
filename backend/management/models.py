from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "Todo", "Todo"
        IN_PROGRESS = "In Bearbeitung", "In Bearbeitung"
        DONE = "Fertig", "Fertig"

    class Priority(models.TextChoices):
        LOW = "Niedrig", "Niedrig"
        MEDIUM = "Mittel", "Mittel"
        HIGH = "Hoch", "Hoch"
        EMERGENCY = "Sonderfall", "Sonderfall"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.LOW)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="created_tasks")
    assigned = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks")

    def __str__(self):
        return f"{self.title} ({self.status}) | Priorität: {self.priority}"