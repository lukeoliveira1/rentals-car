from django.urls import path
from cars.views import paginaInicial, detalheCarro, cadastrarCarro, deletarCarro
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cars_urls'

urlpatterns = [
    path('', paginaInicial, name="paginaInicial"),
    path('detalheCarro/<int:id_produto>/', detalheCarro, name="detalheCarro"), 
    path('cadastrarCarros/', cadastrarCarro, name='cadastrarCarro'),
    path('delete/carro/<int:id>', deletarCarro, name="deletarCarro" ),
] +  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #pra add imagens
