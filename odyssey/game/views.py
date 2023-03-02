from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fractions import Fraction

from json import loads,dumps
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

    






 


    

#servicios en API

#loads -> deseriarisacion


