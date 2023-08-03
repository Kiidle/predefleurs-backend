from django.contrib import admin
from django.contrib.auth import get_user_model
from about.models import Opening, About

User = get_user_model()

admin.site.register(About)
admin.site.register(Opening)