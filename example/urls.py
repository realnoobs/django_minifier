from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("example.app.urls")),
    path("admin/", admin.site.urls),
]
