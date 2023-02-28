from django.contrib import admin
from django.urls import path

from .views import product_and_random

urlpatterns = [
    path("", product_and_random),
]

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)