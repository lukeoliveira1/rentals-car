from django.urls import path
from .views import *

app_name = 'alugueis_urls'

urlpatterns = [
    path('cadastrarLocacao/', cadastrarLocacao, name='cadastrarAluguel'),
    path('listarLocacoes/', listarLocacoes, name='listarLocacoes'),
    path('delete/locacao/<int:id>', deletarLocacao, name="deletarLocacao" ),
]
