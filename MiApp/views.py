from django.shortcuts import render
from MiApp.models import haga_su_pedido, tipo_de_postre, tipo_de_relleno 

def mostrar_index(request):
   return render(request, 'index.html')


def mostrar_pedido(request):
   pedido1 = haga_su_pedido(nombre = '', e_mail = '', cantidad_de_personas ='', nombre_torta='', relleno='', crocante='', numero_de_pisos=''),
   return render(request, 'haga_su_pedido.html' ,{'haga_su_pedido':[pedido1]})


def nuevo_pedido(request):
   if request.method == 'post':
      Nuevo_pedido = haga_su_pedido(nombre=request.post['nombre'], e_mai=request.post['e_mai'], cantidad_de_personas=request.post['cantidad_de_personas'])
      Nuevo_pedido.save()
      return render(request, 'tipo_de_postre.html')
   return render(request, 'crear_nuevo_pedido.html')


def mostrar_tipo_de_postre(request):
   if request.method == 'post':
      pedido_postre = tipo_de_postre(cantidad_de_personas=request.post['cantidad_de_personas'], nombre_torta=request.post['nombre_torta'], relleno=request.post['relleno'])
      pedido_postre.save()        
   return render(request, 'tipo_de_relleno.html')


  
def mostrar_tipo_de_relleno(request):
   pedido_relleno = tipo_de_relleno(relleno = 'chocolate y dulcedeleche', crocante = 'mani', numero_de_pisos = 3 )
   return render(request, 'index.html' ,{'tipo_de_relleno':[pedido_relleno]})