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

class userMascota(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)
    contrasenia = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
    


    
from django.db import models

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)  # como VET001

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

class Cita(models.Model):
    propietario = models.ForeignKey(userMascota, on_delete=models.CASCADE)
    nombre_mascota = models.CharField(max_length=100)
    
    TIPO_MASCOTA = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Conejo', 'Conejo'),
        ('Ave', 'Ave'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]
    tipo_mascota = models.CharField(max_length=20, choices=TIPO_MASCOTA)

    fecha = models.DateField()
    hora = models.TimeField()

    motivo = models.TextField(blank=True)

    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_mascota} ({self.fecha} {self.hora})"
    
class NuevaCita(models.Model):
    propietario = models.ForeignKey(userMascota, on_delete=models.CASCADE)
    nombre_mascota = models.CharField(max_length=100)
    TIPO_MASCOTA = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Conejo', 'Conejo'),
        ('Ave', 'Ave'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]
    tipo_mascota = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_mascota} con {self.veterinario.nombre} el {self.fecha} a las {self.hora}"



class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
