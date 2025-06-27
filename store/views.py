from django.shortcuts import render
from .templates import *


# Create your views here.
def home(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

from django.shortcuts import render, redirect
from .models import Usuario, Producto, Mascota

# Vistas generales
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mi_app/usuarios.html', {'usuarios': usuarios})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_app/productos.html', {'productos': productos})

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mi_app/mascotas.html', {'mascotas': mascotas})
