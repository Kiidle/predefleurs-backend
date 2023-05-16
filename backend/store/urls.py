from django.contrib import admin
from django.urls import include
from django.urls import path

urlpattern = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("cloud/", include("forum.urls")),
    path("forum/", include("forum.urls")),
    path("management/", include("forum.urls")),
    path("media/", include("media.urls")),
    path("shop/", include("store.urls")),
]
