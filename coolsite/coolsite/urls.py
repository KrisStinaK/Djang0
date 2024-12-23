from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from coolsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sportsman.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
