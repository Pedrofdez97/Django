from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from futbol.models import Futbolista


def inicio(request):
    lista_futbolista = Futbolista.objects.all()

    return render(request, 'index.html', {'juga': lista_futbolista})
def equipo(request):
    return render(request, 'equipo.html')
def crearJugador(request):

    if request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        jugador = Futbolista()
        jugador.id = request.POST.get('id')
        jugador.nombre = request.POST.get('nombre')
        jugador.equipo = request.POST.get('equipo')
        jugador.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        Futbolista.save(jugador)
        return redirect('/futbol/index/')
    else:
        return render(request, 'crearjugadores.html')
def crearEquipo(request):
    return render(request, 'crearEquipo.html')


def jugadores(request, id):
   if request.method == 'GET':
       jugadores = Futbolista.objects.get(id=id)
       return render(request,'jugadores.html', {"jug": jugadores})
   else:
       jugadores = Futbolista.objects.get(id=id)
       jugadores.id = request.POST.get('id')
       jugadores.nombre = request.POST.get ('nombre')
       jugadores.equipo = request.POST.get('equipo')
       jugadores.fecha_nacimiento = request.POST.get('fecha_nacimiento')
   return redirect('/futbol/jugadores/')

