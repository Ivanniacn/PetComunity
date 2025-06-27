
from django.contrib import admin
from django.urls import path
from store.views import *

urlpatterns = [
    path('',home,name="home"),
    path('carrito',carrito,name="carrito"),
]

from django.urls import path
from ... import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('productos/', views.lista_productos, name='productos'),
    path('mascotas/', views.lista_mascotas, name='mascotas'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
]
from django.urls import path
from ... import views

urlpatterns = [
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('productos/', views.lista_productos, name='productos'),
    path('mascotas/', views.lista_mascotas, name='mascotas'),
]
