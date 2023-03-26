from django.contrib import admin
from django.urls import path

from .views import frontpage, how_to_use, JSON_samples

urlpatterns = [
    path("", frontpage.as_view()),
    path("how_to_use/", how_to_use.as_view()),
    path("JSON_samples/", JSON_samples.as_view()),
]