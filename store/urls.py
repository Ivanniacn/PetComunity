from django.urls import path
from store import views
from .views import *

urlpatterns = [
    # Añade aquí las rutas que necesites
    path('',home,name='home'),
    path('usuarios/', gestion_usuarios, name='gestion_usuarios'),
 path('productos/', views.productos, name='productos'),
    path('gestion/', views.gestion_productos, name='gestion_productos'),
    path('mascotas/', gestion_mascotas, name='gestion_mascotas'),
    path('', lista_productos, name='lista_productos'),
]
