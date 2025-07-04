from django.shortcuts import render
from django.contrib import messages
from .templates import *
from rest_framework import viewsets
from .serializers import ProductoSerializer


# Create your views here.
def home(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def citas(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'citasMedicas.html', {'veterinarios': veterinarios})


def login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')

        try:
            usuario = userMascota.objects.get(correo=correo, contrasenia=contrasenia)
            request.session['usuario_id'] = usuario.id  # Guardar ID en sesión
            request.session['usuario_nombre'] = usuario.nombre
            messages.success(request, f"Bienvenido, {usuario.nombre}")
            return redirect('home')  # Cambia esto por la ruta de inicio
        except userMascota.DoesNotExist:
            messages.error(request, "Correo o contraseña incorrectos")
    
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # Borra toda la sesión
    return redirect('home')  # O redirige al home si prefieres


def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasenia = request.POST.get('contrasenia')
        confirmar_contrasenia = request.POST.get('confirmar_contrasenia')

        # Verificar que las contraseñas coincidan
        if contrasenia != confirmar_contrasenia:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'registro.html')

        # Verificar si el correo ya está registrado
        if userMascota.objects.filter(correo=correo).exists():
            messages.error(request, "Este correo ya está registrado.")
            return render(request, 'registro.html')

        # Crear nuevo usuario
        nuevo_usuario = userMascota(
            nombre=nombre,
            correo=correo,
            contrasenia=contrasenia  # En producción, se debería encriptar
        )
        nuevo_usuario.save()

        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect('login')  # Asegúrate de tener una vista de login
    return render(request, 'registro.html')

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



def agendar_cita(request):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes iniciar sesión para agendar una cita.")
        return redirect('login')

    propietario = userMascota.objects.get(id=request.session['usuario_id'])

    if request.method == 'POST':
        nombre_mascota = request.POST.get('nombre_mascota')
        tipo_mascota = request.POST.get('tipo_mascota')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo', '')
        veterinario_id = request.POST.get('veterinario')

        veterinario = Veterinario.objects.get(id=veterinario_id)

        Cita.objects.create(
            propietario=propietario,
            nombre_mascota=nombre_mascota,
            tipo_mascota=tipo_mascota,
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            veterinario=veterinario
        )

        messages.success(request, "¡Cita agendada exitosamente!")
        return redirect('agendar_cita')

    veterinarios = Veterinario.objects.all()
    citas_usuario = Cita.objects.filter(propietario=propietario).order_by('-fecha', '-hora')

    return render(request, 'citasMedicas.html', {
        'veterinarios': veterinarios,
        'citas_usuario': citas_usuario
    })
