from django.db import models

# Create your models here.

class Facciones(models.Model):
    nombre= models.CharField(max_length=40)
    raza= models.CharField(max_length=40)
class Hobbits(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)
class Elfo(models.Model):
    nombre = models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)
class Enano(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)
class Orco(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)
