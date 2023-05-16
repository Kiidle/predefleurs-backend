from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()

class Task(models.Model):
    class Status(models.TextField):
        TODO = "Todo", "Todo"
        IN_PROGRESS = "In Bearbeitung", "In Bearbeitung"
        DONE = "Fertig", "Fertig"

    class Priority(models.TextField):
        LOW = "Niedrig", "Niedrig"
        MEDIUM = "Mittel", "Mittel"
        HIGH = "Hoch", "Hoch"
        EMERGENCY = "Sonderfall", "Sonderfall"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="created_tasks")
    assigned = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="tasks")