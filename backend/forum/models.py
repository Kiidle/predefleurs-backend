from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()

class Feedback(models.Model):
    stars = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="feedback")

    def __str__(self):
        return f"{self.author.username} gave {self.stars} Stars"

class SupportRequest(models.Model):
    class Status(models.TextChoices):
        OPEN = "Offen", "Offen"
        QUEUE = "Warteschlange", "Warteschlange"
        TREATED = "In Behandlung", "In Behandlung"
        RESOLVED = "Gelöst", "Gelöst"
        DENIED = "Abgelehnt", "Abgelehnt"

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.OPEN)
    archived = models.BooleanField(null=False, default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supportrequests")
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"Support Request by {self.creator.username}: {self.status}"