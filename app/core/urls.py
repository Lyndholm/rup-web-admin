from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("rup.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]
