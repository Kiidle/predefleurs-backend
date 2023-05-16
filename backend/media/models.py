from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

User = get_user_model()

class Feed(models.Model):
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='static/images/uploads/feed')
    published_date = models.DateTimeField(auto_now_add=True)
    visibility = models.BooleanField(null=False, default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feeds")

    def time_since_published(self):
        now = timezone.now()
        diff = now - self.published_date

        if diff.days >= 365:
            count = diff.days // 365
            return "Vor {count} Jahr{plural}".format(count=count, plural='e' if count > 1 else '')
        elif diff.days >= 30:
            count = diff.days // 30
            return "Vor {count} Monat{plural}".format(count=count, plural='e' if count > 1 else '')
        elif diff.days > 0:
            return "Vor {count} Tag{plural}".format(count=diff.days, plural='e' if diff.days > 1 else '')
        elif diff.seconds >= 3600:
            count = diff.seconds // 3600
            return "Vor {count} Stunde{plural}".format(count=count, plural='n' if count > 1 else '')
        elif diff.seconds >= 60:
            count = diff.seconds // 60
            return "Vor {count} Minute{plural}".format(count=count, plural='n' if count > 1 else '')
        else:
            return "Gerade eben"

    def get_profile_url(self):
        if self.author.pp and hasattr(self.author.pp, 'url'):
            return self.author.pp.url

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-published_date', "-id"]


class FeedLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return '{} liked {}'.format(self.user.username, self.feed.description)

class Commentary(models.Model):
    content = models.TextField(max_length=200)
    published_date = models.DateField(auto_now_add=True)
    reference = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="commentaries")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentaries")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-published_date', "-id"]