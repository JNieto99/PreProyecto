from django.db import models

# Create your models here.
class Animal(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    etapa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo.capitalize()}"