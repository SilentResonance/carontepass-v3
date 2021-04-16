from django.urls import include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    re_path(r'^index.html$', TemplateView.as_view(template_name="commons/index.html")),
    re_path(r'^login.html$', TemplateView.as_view(template_name="commons/login.html")),
]