from django.urls import path
from cars.views import CarBulkUpdate, CarListView, CarCreateView, CarUpdateView, CarDeleteView, CarDetailView, index
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cars_urls'

urlpatterns = [
    path('', index, name="index"),
    path('cars/detail/<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('cars/create/', CarCreateView.as_view(), name='create'),
    path('cars/', CarListView.as_view(), name='list'),
    path('cars/update/<int:pk>/', CarUpdateView.as_view(), name='update'),
    path('cars/delete/<int:pk>', CarDeleteView.as_view(), name="delete" ),
    path('bulk_update/', CarBulkUpdate.as_view(), name='car_bulk_update'),
] +  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #pra add imagens
