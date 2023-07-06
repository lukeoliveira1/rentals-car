from django.urls import path
from .views import *

app_name = 'users_urls'

urlpatterns = [
    path('conta/login/', my_login, name="login"),
    path('conta/logout/', logout_request, name='logout'),
    path("conta/registrar/", register, name="registrar"),
    path('cadastrarClientes/', cadastrarCliente, name='cadastrarCliente'),
    path('clientes/listarClientes/', listarClientes, name='listarClientes'),
    path('delete/cliente/<int:id>', deletarCliente, name="deletarCliente" ),
]
