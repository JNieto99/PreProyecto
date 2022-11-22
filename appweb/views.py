from django.shortcuts import render
from django.http import HttpResponse
from appweb.models import Animal
from django.views.generic import ListView

# Create your views here.

def inicio(request):
    return render(request, "appweb/inicio.html")


def adoptar(request):

    animales = Animal.objects.all()

    contexto = {"listado_animales": animales}

    return render(request, "appweb/Adoptar.html",contexto)