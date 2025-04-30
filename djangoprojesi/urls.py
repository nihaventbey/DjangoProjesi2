from django.contrib import admin
from django.urls import path, include

# 🌟 Eklememiz gereken satırlar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# 🌟 Geliştirme sırasında medya dosyalarını sun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
