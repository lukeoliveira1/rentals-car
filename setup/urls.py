from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carros.urls', namespace='carros_urls')),
    path('', include('usuarios.urls', namespace='usuarios_urls')),
    path('', include('alugueis.urls', namespace='alugueis_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
