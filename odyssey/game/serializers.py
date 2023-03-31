from rest_framework import serializers
from . models import Reto,Jugadores,Usuarios,Partidas
#Usuarios,Partidas

class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

#Serializar los campos, hace la conversion de json a un registro de la base de datos
class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','password')

class PartidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partidas
        fields = ('id','fecha','id_usuario','minutos_jugados','puntaje')