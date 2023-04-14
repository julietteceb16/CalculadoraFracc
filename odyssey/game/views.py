from django.shortcuts import render
from rest_framework import viewsets
from . serializers import RetoSerializer,JugadorSerializer,UsuariosSerializer,PartidasSerializer
from .models import Reto,Jugadores,Usuarios,Partidas
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests
from random import randrange



#load cargar un string y convertirlo en json y dump un objeto de jsaon convertirlo en string 

# Create your views here.

#jason intercambaiar datos entre compus,  la strign se comvierte en una lista 

#invocar con funciones: 


class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)
    

    
def index(request):
    #return HttpResponse('<h1> Hola Mundo! </h1>')
    return render(request,'index.html')


def proceso(request):
    nombre = request.POST['nombre']
    nombre= nombre.upper()
    return HttpResponse('Hola '+ nombre)


@csrf_exempt
def registro(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']
    password = body['password']
    group = body['group']
    datos = (username,password,group)
    message ={'message': 'Registro exitoso' }
    return HttpResponse(dumps(message),datos, content_type='application/json')

def juego(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    username = body['username']

    if username == 'eg_user' :
        message = {'message': 'Usuario autenticado'}
    else:
        message = {'message': 'Usuario no autenticado'}
    return HttpResponse(dumps(message), content_type='application/json')
    



def bienvenida(request):
    letrero="Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    p = request.GET['p']
    q = request.GET['q']
    r = int(p) * int(q)
    return HttpResponse("La multiplicacion de " +p+ "x" +q+" = " +str(r))#reciviendo 1 parametro para mas de dos parametros poner "&"
#http://127.0.0.1:8000/multiplicacion?p=10&q=2 --> para que lo resuelva

@csrf_exempt#la funcion va a hacer extenga del toque de seguridad, crea codigo que permite que division sea excenta del token 
def division(request):
    body_unicode = request.body.decode('utf-8')#como puede contener acentos se usa utf-8
    body = loads(body_unicode)#esto es json donde se va a buscar el elemento p y q 
    p = body['p']#esto deberia ser entero
    q = body['q']
    resultado = Fraccion(p,q)
    json_resultado = resultado.toJSON() #Se paso a jason

    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")


@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    #num_resultado = num1 + num2
    #den_resultado = den1 + den2
    if den1 == den2:
        den_resultado = den1
        num_resultado = num1 + num2
    else:
        den_resultado = den1 * den2
        num_resultado = int(((den_resultado/den1)*num1)+((den_resultado/den2)*num2))
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")


@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    if den1 == den2:
        den_resultado = den1
        num_resultado = num1 - num2
    else:
        den_resultado = den1 * den2
        num_resultado = int(((den_resultado/den1)*num1)-((den_resultado/den2)*num2))
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")

@csrf_exempt
def multifrac(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    num_resultado = num1 * num2
    den_resultado = den1 * den2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")
        

@csrf_exempt
def divfrac(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    num1 = body['num1']
    den1 = body['den1']
    num2 = body['num2']
    den2 = body['den2']
    num_resultado = num1 * den2
    den_resultado = den2 * num2
    resultado = Fraccion(num_resultado,den_resultado)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json, content_type = "text/json-comment-filtered")


@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        lista =[]  
        for registro in resultado:
            id,grupo,grado,numero = registro
            diccionario = {"id":id,"grupo":grupo,"grado":grado,"num_lista":numero}
            lista.append(diccionario)
        #registros =[{"id":1,"grupo":"A","grado":6,"num_lista":4},{"id":2,"grupo":"B","grado":6,"num_lista":2}] 
        registros = lista
        return render(request, 'usuarios.html',{'lista_usuarios':registros})
    elif request.method == 'POST':
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        grado = eljson['grado']
        grupo = eljson['grupo']
        num_lista = eljson['num_lista']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)",(grupo, grado, num_lista))
        con.commit()
        return HttpResponse('OK')
    elif request.method == 'DELETE':
        return(usuarios_d(request))


@csrf_exempt
def usuarios_p(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)",(grupo, grado, num_lista))
    con.commit()
    return HttpResponse('OK')


@csrf_exempt
def usuarios_d(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE id_usuario=?",(str(id)))
    con.commit()
    return HttpResponse('OK usuario borrado'+str(id))



#servicio endpoint de validación de usuarios
#entrada: { "id_usuario" :"usuario","pass" : "contrasenia"}
#salida: {"estatus":True}
@csrf_exempt
def valida_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    usuario  = eljson['id_usuario']
    contrasenia = eljson['pass']
    print(usuario+contrasenia)
    #con = sqlite3.connect("db.sqlite3")
    #cur = con.cursor()
    #res = cur.execute("SELECT * FROM usuarios WHERE id_usuario=? AND password=?",(str(usuario),str(contrasenia)))
    #si el usuario es correcto regresar respuesta exitosa 200 OK
    #en caso contrario, regresar esatus false
    return HttpResponse('{"estatus":true}')


#Ruta para carga de la página web con el formulario de login
@csrf_exempt
def login(request):
    return render(request, 'login.html')

#Ruta para el proceso del login (invocación del servicio de verificación de usuario)
@csrf_exempt
def procesologin(request):
    usuario = request.POST['usuario']
    contrasenia = request.POST['password']
    #invoca el servicio de validación de usuario
    url = "http://127.0.0.1:8000/valida_usuario"
    header = {
    "Content-Type":"application/json"
    }
    payload = {   
    "id_usuario" :usuario,
    "pass" : contrasenia
    }
    result = requests.post(url,  data= dumps(payload), headers=header)
    if result.status_code == 200:
        return HttpResponse('Abrir página principal')
    return HttpResponse('Abrir página de credenciales inválidas')

##Viewset hace todas las vistas para hacer los 4 comandos

class RetoViewSet(viewsets.ModelViewSet):
    queryset = Reto.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = RetoSerializer
    
#### "METODO REST #####
class JugadoresViewSet(viewsets.ModelViewSet): #va hacer las 4 vistas(insertar, enlistar, etc) de tipo jugador
    queryset = Jugadores.objects.all() #select * from Calculadora.Jugadores
    serializer_class = JugadorSerializer

########
class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = PartidasSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all() #all recupera todos los registro de la entidada Reto
    serializer_class = UsuariosSerializer

#########


def grafica(request):
    #h_var : The title for horizontal axis
    h_var = 'X'#nombre al eje x 

    #v_var : The title for horizontal axis
    v_var = 'Y'#nombre al eje y

    #data : A list of list which will ultimated be used 
    # to populate the Google chart.
    data = [[h_var,v_var]]
    """
    An example of how the data object looks like in the end: 
        [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
    The first list will consists of the title of horizontal and vertical axis,
    and the subsequent list will contain coordinates of the points to be plotted on
    the google chart
    """

    #The below for loop is responsible for appending list of two random values  
    # to data object
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])

    #h_var_JSON : JSON string corresponding to  h_var
    #json.dumps converts Python objects to JSON strings
    h_var_JSON = dumps(h_var)#horizontal

    #v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = dumps(v_var)#vertical

    #modified_data : JSON string corresponding to  data
    modified_data = dumps(data)

    #Finally all JSON strings are supplied to the charts.html using the 
    # dictiory shown below so that they can be displayed on the home screen
    return render(request,"charts.html",{'values':modified_data,'h_title':h_var_JSON,'v_title':v_var_JSON})#pasae los datos 

# def barras(request):
#     '''
#     data = [
#           ['Jugador', 'Minutos Jugados'],
#           ['Ian', 1000],
#           ['Héctor', 1170],
#           ['Alan', 660],
#           ['Manuel', 1030]
#         ]
#     '''
#     data = []
#     data.append(['Jugador', 'Minutos Jugados'])#se agrega la primera fila
#     resultados = Reto.objects.all() #select * from reto;    #-->mandar a llamar un servicio(rest)
#     titulo = 'Videojuego Odyssey' 
#     titulo_formato = dumps(titulo) #formatear json --> IMPORTANTE
#     subtitulo= 'Total de minutos por jugador' 
#     subtitulo_formato = dumps(subtitulo)#formatear json --> IMPORTANTE
#     if len(resultados)>0:
#         for registro in resultados:#Itero los resuktados y saco nombre
#             nombre = registro.nombre
#             minutos = registro.minutos_jugados
#             data.append([nombre,minutos])#se agrega a la data
#         data_formato = dumps(data) #formatear data en string para JSON
#         elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
#         return render(request,'barras.html',elJSON)#datos de los campos al html --> a barras
#     else:
#         return HttpResponse("<h1> No hay registros a mostrar</h1>")



#def gauge(request):
    #'''
    #data = [
          #['Jugador', 'Minutos Jugados'],
          #['Ian', 1000],
          #['Héctor', 1170],
          #['Alan', 660],
          #['Manuel', 1030]
        #]
    #'''
    #data = []
    #data.append(['Jugador', 'Minutos Jugados'])#se agrega la primera fila
    #resultados = Reto.objects.all() #select * from reto;    #-->mandar a llamar un servicio(rest)
    #titulo = 'Videojuego Odyssey' 
    #titulo_formato = dumps(titulo) #formatear json --> IMPORTANTE
    #subtitulo= 'Total de minutos por jugador' 
    #subtitulo_formato = dumps(subtitulo)#formatear json --> IMPORTANTE
    #if len(resultados)>0:
        #for registro in resultados:#Itero los resuktados y saco nombre
            #nombre = registro.nombre
            #minutos = registro.minutos_jugados
            #data.append([nombre,minutos])#se agrega a la data
        #data_formato = dumps(data) #formatear data en string para JSON
        #elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
        #return render(request,'gauge.html',elJSON)#datos de los campos al html --> a barras
    #else:
        #return HttpResponse("<h1> No hay registros a mostrar</h1>")




@csrf_exempt
def barras(request):
    url = "http://127.0.0.1:8000/consultar_db"
    response = requests.get(url)
    data = loads(response.content)['losDatos']
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    elJSON = {'losDatos': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
    return render(request,'barras.html',elJSON)

# el parametro de entrada que sean minutos jugados y filtrar la base y para ver quien tiene  el mayor numero de  minutos jugados
@csrf_exempt
def basedatos(request):
    if(request.method == 'POST'):
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        minutos = eljson['minutos_jugados']
        
        resultados = Reto.objects.filter(minutos_jugados__gt=minutos)
        data = [['Nombre', 'Minutos jugados']]
        for registro in resultados:
            nombre = registro.nombre
            minutos = registro.minutos_jugados
            data.append([nombre, minutos])
        data_json = dumps({'losDatos': data})
        return HttpResponse(data_json, content_type='application/json')

    


def gauge(request):
    url = "http://127.0.0.1:8000/basedatos"
    header = {
    "Content-Type":"application/json"
    }
    payload = {   
    "minutos_jugados":"130"
    }
    result = requests.post(url,  data= dumps(payload), headers=header)
    if result.status_code == 200:
        #sresponse = requests.get(url)
        data = loads(result.content)['losDatos']
        titulo = 'Videojuego Odyssey'
        titulo_formato = dumps(titulo)
        subtitulo= 'Total de minutos por jugador'
        subtitulo_formato = dumps(subtitulo)
        elJSON = {'losDatos': data, 'titulo': titulo_formato, 'subtitulo': subtitulo_formato}
        return render(request,'gauge.html',elJSON)



 #get enlisto
 #post inserto


    

#servicios en API

#loads -> deseriarisacion


