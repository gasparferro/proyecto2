from django.http import HttpResponse
import datetime
from django.template import Template, context
from django.template import loader

def saludo(request): 
    return HttpResponse(" hola chango ")

def segunda_vista(request):
    return HttpResponse("<br><br>esto es facil ")

def diadehoy(request):
    dia =  datetime.datetime.now()
    documentodetexto = f"hoy es dia: <br>  {dia}"
    return HttpResponse(documentodetexto)

def minombre(self, nombre):
    documentodetexto = f"mi nombre es <br> {nombre} "
    return HttpResponse(documentodetexto)

def plantilla1(self):
    plantilla= loader.get_template("template1.html")
    documento= plantilla.render() 
    return HttpResponse(documento)