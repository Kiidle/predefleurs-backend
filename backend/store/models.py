from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='static/images/uploads/store')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return f"Article: {self.title}"
class Reservation(models.Model):
    class Status(models.TextChoices):
        OPEN = "Offen", "Offen"
        APPROVED = "Angenommen", "Angenommen"
        DENIED = "Abgelehnt", "Abgelehnt"
        DONE = "Abgeschlossen", "Abgeschlossen"

    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name="reservations")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reservations")
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.OPEN)

    def __str__(self):
        return f"{self.user.username} reserverd {self.article.title} on {self.start_date}"