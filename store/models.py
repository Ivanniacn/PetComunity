from django.db import models
import requests

# Create your models here.
class productos(models.Model):
    id= models.CharField(max_length=4,primary_key=True)
    nombreProducto= models.CharField(max_length=200)
    urlProducto= models.CharField(max_length=1000)
    precioProducto= models.IntegerField()
    tipoProducto= models.CharField(max_length=50)
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
