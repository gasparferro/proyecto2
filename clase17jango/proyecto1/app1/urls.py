from django.urls import path 
from app1 import views 

urlpatterns=[


    path('', views.Faccion, name="Inicio"),
    path('hobbits', views.Hobbits, name="hobbits"),
    path('elfos', views.Elfos, name="elfos"),
    path('enanos', views.Enanos, name="enanos"),
    path('orcos', views.Orcos, name="orcos"),
    path('father', views.Cursoformulario, name="formulario")
]
