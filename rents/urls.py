from django.urls import path
from .views import *

app_name = 'rents_urls'

urlpatterns = [
    path('rents', RentListView.as_view(), name='list'),
    path('rents/detail/<int:pk>/', RentDetailView.as_view(), name='detail'),
    path('rents/create/', RentCreateView.as_view(), name='create'),
    path('rents/update/<int:pk>/', RentUpdateView.as_view(), name='update'),
    path('rents/delete/<int:pk>', RentDeleteView.as_view(), name="delete" ),
]
