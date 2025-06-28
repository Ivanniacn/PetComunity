from django.shortcuts import render
from .templates import *
from rest_framework import viewsets
from .serializers import ProductoSerializer


# Create your views here.
def home(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def productos(request):
    productos = ProductoTienda.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def pagina_inicio(request):
    productos = ProductoTienda.objects.all()
    return render(request, 'pagina.html', {'productos': productos})

def gestion(request):
    productos = ProductoTienda.objects.all().order_by('-id')  # <- define esto antes que cualquier return
    form = ProductoForm()

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = get_object_or_404(ProductoTienda, id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion')  # redirige para evitar resubmisión

    elif request.method == 'GET' and 'eliminar' in request.GET:
        producto_id = request.GET.get('eliminar')
        producto = get_object_or_404(ProductoTienda, id=producto_id)
        producto.delete()
        return redirect('gestion')

    return render(request, 'gestion.html', {'productos': productos, 'form': form})
from django.shortcuts import render, redirect
from .models import Usuario, Mascota

# Vistas generales
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mi_app/usuarios.html', {'usuarios': usuarios})

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mi_app/mascotas.html', {'mascotas': mascotas})

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def gestion_mascotas(request):
    mascotas = Mascota.objects.select_related('dueño').all().order_by('-id')
    form = MascotaForm()

    if request.method == 'POST':
        mascota_id = request.POST.get('mascota_id')
        if mascota_id:
            mascota = get_object_or_404(Mascota, id=mascota_id)
            form = MascotaForm(request.POST, instance=mascota)
        else:
            form = MascotaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion_mascotas')

    elif request.method == 'GET' and 'eliminar' in request.GET:
        mascota_id = request.GET.get('eliminar')
        mascota = get_object_or_404(Mascota, id=mascota_id)
        mascota.delete()
        return redirect('gestion_mascotas')

    return render(request, 'mascotas.html', {'mascotas': mascotas, 'form': form})

def gestion_productos(request):
    productos = ProductoTienda.objects.all().order_by('-id')
    form = ProductoForm()

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            producto = get_object_or_404(ProductoTienda, id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion_productos')

    elif request.method == 'GET' and 'eliminar' in request.GET:
        producto = get_object_or_404(ProductoTienda, id=request.GET.get('eliminar'))
        producto.delete()
        return redirect('gestion_productos')

    return render(request, 'gestion.html', {'productos': productos, 'form': form})


def gestion_usuarios(request):
    usuarios = Usuario.objects.all().order_by('-id')
    form = UsuarioForm()

    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if usuario_id:
            usuario = get_object_or_404(Usuario, id=usuario_id)
            form = UsuarioForm(request.POST, instance=usuario)
        else:
            form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestion_usuarios')

    elif request.method == 'GET' and 'eliminar' in request.GET:
        usuario_id = request.GET.get('eliminar')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        usuario.delete()
        return redirect('gestion_usuarios')

    return render(request, 'usuarios.html', {'usuarios': usuarios, 'form': form})


def lista_productos(request):
    productos = ProductoTienda.objects.all().order_by('-id')
    form = ProductoForm()

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        if producto_id:
            # Actualizar producto existente
            producto = get_object_or_404(ProductoTienda, id=producto_id)
            form = ProductoForm(request.POST, instance=producto)
        else:
            # Insertar nuevo producto
            form = ProductoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('lista_productos')

    elif request.method == 'GET' and 'eliminar' in request.GET:
        producto_id = request.GET.get('eliminar')
        producto = get_object_or_404(ProductoTienda, id=producto_id)
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'productos.html', {'productos': productos, 'form': form})
