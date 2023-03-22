from django.contrib import admin
from django.urls import path

from .views import frontpage, how_to_use

urlpatterns = [
    path("", frontpage.as_view()),
    path("how_to_use/", how_to_use.as_view())
]