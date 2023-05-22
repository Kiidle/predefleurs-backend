from django.contrib import admin
from django.contrib.auth import get_user_model
from store.models import Article, Reservation

User = get_user_model()

admin.site.register(Article)
admin.site.register(Reservation)