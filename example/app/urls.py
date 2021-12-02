from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("app/", TemplateView.as_view(template_name="app/index.html"), name="app"),
    path("theme/", TemplateView.as_view(template_name="default/index.html"), name="theme"),
]
