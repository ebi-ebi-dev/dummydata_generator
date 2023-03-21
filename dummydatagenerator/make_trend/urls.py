from django.contrib import admin
from django.urls import path

from .views import make_trend

urlpatterns = [
    path("", make_trend),
]