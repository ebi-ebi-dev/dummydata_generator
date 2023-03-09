from django.contrib import admin
from django.urls import path

from .views import MyCreate, check

urlpatterns = [
    # path("", create),
    path("", MyCreate.as_view(), name='create'),
    path("check/", check), # <- これで、create/checkにできる。
    # path("", create.as_view())
]

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)