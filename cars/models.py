from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacter = models.CharField(max_length=100)
    color = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=4)
    motor = models.CharField(max_length=20, null=True, blank=True)
    fuel_type = models.CharField(max_length=100, null=True, blank=True)
    license_plate = models.CharField(max_length=8, null=True, blank=True, unique=True)
    photo = models.FileField(upload_to='carros', blank=True)

    def __str__(self):
        return self.model