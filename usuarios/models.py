from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    cnh = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.name