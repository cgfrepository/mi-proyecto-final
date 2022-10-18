from django.shortcuts import render
from ejemplo.models import Familiar


# Create your views here.

def index(request):
    suma=1+1
    return render(request, "ejemplo/saludar.html",
    {"nombre":"Cristian",
    "sexo":"masculino",
    "suma":suma})

def index2(request,nombre,apellido):
    suma=1+1
    return render(request, "ejemplo/saludar.html",
    {"nombre":nombre,
    "apellido":apellido})

def index3(request):
    return render(request,"ejemplo/saludar.html",
    {"notas":[5,6,4,6,5,7]})

def imc(request,peso,altura):
    peso = float(peso)
    altura= float(altura)
    altura= altura/100
    imc = peso/(altura**2)
    return render(request,"ejemplo/imc.html",
     {"imc":imc,}
    )

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
  {"lista_familiares": lista_familiares})
