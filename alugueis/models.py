from django.db import models
from carros.models import carro
from usuarios.models import cliente

# Create your models here.
class aluguel(models.Model):
    data_retirada = models.DateField()
    data_entrega = models.DateField()
    valor = models.FloatField()
    cliente =  models.OneToOneField(cliente, on_delete=models.CASCADE)
    carro =  models.OneToOneField(carro, on_delete=models.CASCADE)

    def __str__(self):
        return self.carro.modelo
