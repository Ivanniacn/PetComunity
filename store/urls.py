from django.urls import path
from store import views
from .views import *

urlpatterns = [
    # Añade aquí las rutas que necesites
    path('',home,name='home'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('productos/', views.lista_productos, name='productos'),
    path('mascotas/', views.lista_mascotas, name='mascotas'),
]
