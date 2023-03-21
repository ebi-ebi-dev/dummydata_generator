from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("frontpage.urls")),
    path("product_and_random/", include("gen_product_and_random.urls")),
    path("create/", include("create.urls")),
    path("make_trend/", include("make_trend.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)