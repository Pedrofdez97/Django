from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('index/', inicio),
    path('jugadores/<id>', jugadores),
    path('crearjugador/', crearJugador),
    path('modificar/<int:id>', modifcarJugador),
    path('eliminar/<id>', eliminarjugador)
]