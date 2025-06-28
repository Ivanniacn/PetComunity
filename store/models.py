from django.db import models
import requests

# Create your models here.

from django.db import models

class ProductoTienda(models.Model):
    nombreProducto = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.nombreProducto


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
