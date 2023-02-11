from django.http import HttpResponse
from .models import Pokemon
from django.shortcuts import get_object_or_404, render, redirect
# Aca se crearan las funciones que retornaran los datos de la bbdd para ser usadas en el html.
# Use basicamente las mismas requests ya que no se requeria mucho mas.
# Create your views here.
def index(request):
    title = "welcome to django curse!!"
    return render(request, "index.html", {
        'title' : title
    })
def pokemones50(request):
    pokemones50 = Pokemon.objects.all()
    return render(request, "pokemones50.html", {
        'pokemones50' : pokemones50
    })

def grass(request):
    grass = Pokemon.objects.all()
    return render(request, "grass.html", {
        'grass' : grass
    })

def flying(request):
    flying = Pokemon.objects.all()
    return render(request, "flying.html", {
        "flying" : flying
    })

def peso(request):
    peso = Pokemon.objects.all()
    return render(request, "peso.html", {
        'peso' : peso
    })

def invertidos(request):
    invertidos = Pokemon.objects.all()
    return render(request, "invertidos.html", {
        'invertidos' : invertidos
    })




