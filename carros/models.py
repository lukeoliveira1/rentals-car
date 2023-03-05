from django.db import models

# Create your models here.
class carro(models.Model):
    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    motor = models.CharField(max_length=20)
    velocidade_maxima = models.CharField(max_length=100)
    tipo_combustivel = models.CharField(max_length=100)
    placa = models.CharField(max_length=8)
    numero_chassi = models.CharField(max_length=100)
    capacidade = models.CharField(max_length=100)
    foto = models.FileField(upload_to='carros', blank=True)

    def __str__(self):
        return self.modelo