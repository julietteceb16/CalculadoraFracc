from django.db import models
#represntacion de una tabla 
# Create your models here.
class Reto(models.Model):
    nombre = models.CharField(max_length=30) 
    minutos_jugados = models.IntegerField()

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()



