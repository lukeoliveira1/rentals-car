from django.db import models
from cars.models import Car
from users.models import Client

# Create your models here.
class Rent(models.Model):
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    value = models.FloatField()
    client =  models.OneToOneField(Client, on_delete=models.CASCADE)
    car =  models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.model
