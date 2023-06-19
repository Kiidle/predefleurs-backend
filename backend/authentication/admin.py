from django.contrib import admin
from django.contrib.auth import get_user_model
from authentication.models import Data, Personal, Address, Certificate, Education, Health, Criminal

User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Data)
admin.site.register(Personal)
admin.site.register(Address)
admin.site.register(Certificate)
admin.site.register(Education)
admin.site.register(Health)
admin.site.register(Criminal)