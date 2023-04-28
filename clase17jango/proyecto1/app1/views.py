from django.shortcuts import render
from app1.models import Facciones
from django.http import HttpResponse
from app1.forms import cursoformulario

# Create your views here.
def Faccion(request):
    return render(request, 'app1/faccion.html')
def Hobbits(request):
    return render(request,'app1/hobbits.html')
def Enanos(request):
    return render(request,'app1/enanos.html')
def Elfos(request):
    return render(request,'app1/elfos.html')
def Orcos(request):
    return render(request,'app1/orcos.html')

def Cursoformulario(request):
      if request.method == "POST":
            miFormulario = cursoformulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  faccion = Facciones( nombre = informacion['nombre'],raza=informacion['raza'])
                  faccion.save()
                  return render(request, "app1/father.html")
      else:
            miFormulario = cursoformulario()
 
      return render(request, "app1/father.html", {"miFormulario": miFormulario})