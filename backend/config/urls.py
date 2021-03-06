from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('projects.urls')),
    path('api/v1/', include('news.urls')),
    path('api/v1/', include('subscribe.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

