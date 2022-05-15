from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *

def inicio(request):
    lista_futbolista = Futbolista.objects.all()
    return render(request, 'index.html', {'juga': lista_futbolista})


def eliminarjugador(request, id):
    juga = Futbolista.objects.get(id=id)
    if juga is not None:
        Futbolista.delete(juga)
    return redirect('/futbol/index/')

def crearJugador(request):

    if request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        jugador = Futbolista()
        jugador.id = request.POST.get('id')
        jugador.nombre = request.POST.get('nombre')
        jugador.equipo = request.POST.get('equipo')
        jugador.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        jugador.fecha_debut = request.POST.get('fecha_debut')
        jugador.equipo_debut = request.POST.get('equipo_debut')
        Futbolista.save(jugador)
        return redirect('/futbol/index/')
    else:
        return render(request, 'crearjugadores.html')

def modifcarJugador(request,id):
    if request.method == "GET":
        j = Futbolista.objects.filter(id=id).first()
        return render(request, 'modificar.html', {'j': j})
    else:
        j = Futbolista.objects.get(id=id)
        j.nombre = request.POST.get('nombre')
        j.equipo = request.POST.get('equipo')
        j.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        j.fecha_debut = request.POST.get('fecha_debut')
        j.equipo_debut = request.POST.get('equipo_debut')
        Futbolista.save(j)
        return redirect('/futbol/index/')



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

