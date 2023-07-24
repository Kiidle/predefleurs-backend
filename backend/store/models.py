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

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"Article: {self.title}"

    class Meta:
        ordering = ['-id', "title"]

class Reservation(models.Model):
    class Status(models.TextChoices):
        OPEN = "Offen", "Offen"
        APPROVED = "Angenommen", "Angenommen"
        DENIED = "Abgelehnt", "Abgelehnt"
        READY = "Abholbereit", "Abholbereit"
        DONE = "Abgeschlossen", "Abgeschlossen"

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.OPEN)

    def format_date(self):
        return self.start_date.strftime("%d.%m.%Y %H:%M Uhr")

    def __str__(self):
        return f"{self.user.username} reserverd {self.article.title} on {self.start_date}"

    class Meta:
        ordering = ['-start_date']