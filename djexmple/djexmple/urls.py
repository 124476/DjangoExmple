from django.conf import settings
import django.conf.urls.static
import django.contrib
import django.contrib.auth.urls
from django.urls import include, path

urlpatterns = [
    path("", include("homepage.urls")),
    path("users/", include("users.urls")),
    path("admin/", django.contrib.admin.site.urls),
]

urlpatterns += django.conf.urls.static.static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)

urlpatterns += django.conf.urls.static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
