from django.urls import path
from .views import *

app_name = 'users_urls'

urlpatterns = [
    path('conta/login/', LoginView.as_view(), name="login"),
    path('conta/logout/', LogoutView.as_view(), name='logout'),
    path("conta/registrar/", RegisterView.as_view(), name="registrar"),
    path('clients', ClientListView.as_view(), name='list'),
    path('clients/detail/<int:pk>/', ClientDetailView.as_view(), name='detail'),
    path('clients/create/', ClientCreateView.as_view(), name='create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='update'),
    path('clients/delete/<int:pk>', ClientDeleteView.as_view(), name="delete" ),
]
