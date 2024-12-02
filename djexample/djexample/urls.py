from django.conf import settings
import django.conf.urls.static
import django.contrib
import django.contrib.auth.urls
from django.urls import include, path

urlpatterns = [
    path("", include("homepage.urls")),
    path("auth/", include("users.urls")),
    path("auth/", include("allauth.urls")),
    path("admin/", django.contrib.admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += django.conf.urls.static.static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)

urlpatterns += django.conf.urls.static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
