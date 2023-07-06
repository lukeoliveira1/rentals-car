from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls', namespace='cars_urls')),
    path('', include('users.urls', namespace='users_urls')),
    path('', include('rents.urls', namespace='rents_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
