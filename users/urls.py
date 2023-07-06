from django.urls import path
from .views import *

app_name = 'users_urls'

urlpatterns = [
    path('conta/login/', my_login, name="login"),
    path('conta/logout/', logout_request, name='logout'),
    path("conta/registrar/", register, name="registrar"),
    path('clients', ClientListView.as_view(), name='list'),
    path('clients/detail/<int:pk>/', ClientDetailView.as_view(), name='detail'),
    path('clients/create/', ClientCreateView.as_view(), name='create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='update'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name="delete" ),
]
