from django.db import models

# Create your models here.
class Perro(models.Model):
    
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    etapa = models.CharField(max_length=50)

    def __str__(self):
        return f"Raza: {self.raza} | Nombre: {self.nombre}"

class Gato(models.Model):
    
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    etapa = models.CharField(max_length=50)

    def __str__(self):
        return f"Raza: {self.raza} | Nombre: {self.nombre}"

class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre.capitalize()}"