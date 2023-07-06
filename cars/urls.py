from django.urls import path
from cars.views import CarListView, CarCreateView, CarUpdateView, CarDeleteView, CarDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cars_urls'

urlpatterns = [
    path('cars', CarListView.as_view(), name="index"),
    path('cars/detail/<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('cars/create/', CarCreateView.as_view(), name='create'),
    path('cars/update/<int:pk>/', CarUpdateView.as_view(), name='update'),
    path('cars/delete/<int:pk>', CarDeleteView.as_view(), name="delete" ),
] +  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #pra add imagens
