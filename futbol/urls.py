from django.urls import path
from . import views
from .views import inicio, jugadores, equipo, crearEquipo, crearJugador

urlpatterns = [
    path('index/', inicio),
    path('jugadores/<id>', jugadores),
    path('equipo/', equipo),
    path('crearequipo/', crearEquipo),
    path('crearjugador/', crearJugador),
]