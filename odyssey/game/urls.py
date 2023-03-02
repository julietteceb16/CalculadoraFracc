from django.urls import path
from . import views #el punto significa impotar todo de views


urlpatterns = [
    path('',views.index, name='index'), #el primero es para cachar expresiones regulares(cualquier texto), el segundo dice como se va a llamar la clase y el final ek nombre de la clase
    path('proceso',views.proceso,name='proceso'),#cundo el usuario ponga proceso tienes que irte a viewa y enontrar proceso
    path('bienvenida',views.bienvenida,name='bienvenida'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.division,name='division'),
    path('suma',views.suma,name='suma'),
    path('resta',views.resta,name='resta'),
    path('multifrac',views.multifrac,name='multifrac'),
    path('divfrac',views.divfrac,name='divfrac'),
       

]

