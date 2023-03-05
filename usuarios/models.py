from django.db import models

# Create your models here.
class cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=12)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    numero_cnh = models.CharField(max_length=50)

    def __str__(self):
        return self.nome