from django.contrib import admin
from django.urls import path

from .views import frontpage

urlpatterns = [
    path("", frontpage.as_view())
]