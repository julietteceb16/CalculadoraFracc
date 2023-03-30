from django.urls import include,path
from rest_framework import routers
from . import views #el punto significa impotar todo de views

#rutas
router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)
router.register(r'partida', views.PartidasViewSet)
router.register(r'usuario', views.UsuariosViewSet)


urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'), #el primero es para cachar expresiones regulares(cualquier texto), el segundo dice como se va a llamar la clase y el final ek nombre de la clase
    path('proceso',views.proceso,name='proceso'),#cundo el usuario ponga proceso tienes que irte a viewa y enontrar proceso
    path('registro',views.registro,name= 'registro'),
    path('login',views.login, name='login'),
    path('bienvenida',views.bienvenida,name='bienvenida'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.division,name='division'),
    path('suma',views.suma,name='suma'),
    path('resta',views.resta,name='resta'),
    path('multifrac',views.multifrac,name='multifrac'),
    path('divfrac',views.divfrac,name='divfrac'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d,name='usuarios_d'),
    path('valida_usuario',views.valida_usuario, name='valida_usuario'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),



    
   
       

]

