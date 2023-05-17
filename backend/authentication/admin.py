from django.contrib import admin
from django.contrib.auth import get_user_model
from authentication.models import Data, Address

User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Data)
admin.site.register(Address)