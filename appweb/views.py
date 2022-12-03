from django.shortcuts import render
from django.http import HttpResponse
from appweb.models import Perro, Gato, Personas
from django.views.generic import ListView

# Create your views here.

def inicio(request):
    return render(request, "appweb/inicio.html")


def adoptar(request):

    can = Perro.objects.all()

    contexto = {"listado_perritos": can}

    return render(request, "appweb/Perros.html",contexto)

def adoptar2(request):

    michi = Gato.objects.all()

    contexto = {"listado_gatitos": michi}

    return render(request, "appweb/Gatos.html",contexto)

def form_perros(request):

    if request.method == 'POST':

        nombre_can = request.POST['nombre']
        etapa_can = request.POST['etapa']
        raza_can = request.POST['raza']

        perro = Perro(nombre=nombre_can,etapa=etapa_can,raza=raza_can)
        
        perro.save()

    return render(request, "appweb/Reg_perros.html")

def form_gatos(request):

    if request.method == 'POST':

        nombre_michi = request.POST['nombre']
        etapa_michi = request.POST['etapa']
        raza_michi = request.POST['raza']

        gato = Gato(nombre=nombre_michi,etapa=etapa_michi,raza=raza_michi)
        
        gato.save()

    return render(request, "appweb/Reg_gatos.html")

def formapers(request):

    if request.method == 'POST':

        nomb = request.POST['nomb']
        apell = request.POST['apell']
        tel = request.POST['tel']

        persona = Personas(nombre=nomb,apellido=apell,telefono=tel)
        
        persona.save()

    return render(request, "appweb/RegPersonas.html")

def daradop(request):
    return render(request, "appweb/DarAdopta.html")

def bus_perro(request):
    return render (request, "appweb/Perros.html")


def res_perro(request):
    return render (request, "appweb/Perro_res.html")

def bus_gato(request):
    return render (request, "appweb/Gatos.html")


def res_gato(request):
    nombre_michi = request.GET["nombre"]

    name = Gato.objects.filter(nombre__icontains=nombre_michi)

    return render (request, "appweb/Gato_res.html",{"Nombres":name})