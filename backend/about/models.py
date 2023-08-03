from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import Group

User = get_user_model()


class About(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='static/images/uploads/about', null=True, blank=True)

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"Über uns: {self.title}"

    class Meta:
        ordering = ['number', "title"]


class Opening(models.Model):
    class Day(models.TextChoices):
        MONDAY = "Montag", "montag",
        TUESDAY = "Dienstag", "dienstag"
        WEDNESDAY = "Mittwoch", "mittwoch"
        THURSDAY = "Donnerstag", "donnerstag"
        FRIDAY = "Freitag", "freitag"
        SATURDAY = "Samstag", "samstag"
        SUNDAY = "Sonntag", "sonntag"

    day = models.CharField(max_length=50, choices=Day.choices)
    time_morning_from = models.TimeField(null=True, blank=True)
    time_morning_to = models.TimeField(null=True, blank=True)
    time_afternoon_from = models.TimeField(null=True, blank=True)
    time_afternoon_to = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.day}: {self.time_morning_from} - {self.time_morning_to} & {self.time_afternoon_from} - {self.time_afternoon_to}"

