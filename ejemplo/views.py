from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar,FamiliarForm 
from django.views import View


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

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
        

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})