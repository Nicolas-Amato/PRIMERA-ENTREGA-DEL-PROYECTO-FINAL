from django.shortcuts import render
from MiApp.models import haga_su_pedido, tipo_de_postre, tipo_de_relleno 

def mostrar_index(request):
   return render(request, 'index.html')

def nuevo_pedido(request):
   if request.method == 'post':
      mostrar_pedido = mostrar_pedido (nombre=request.post['nombre'], e_mai=request.post['e_mai'], cantidad_de_personas=request.post['cantidad_de_personas'])
      mostrar_pedido.save()
      return render(request, 'index.html')
      
   return render(request, 'crear_nuevo_pedido.html')


def mostrar_pedido(request):
   pedido1 = haga_su_pedido(nombre = 'rodolfo', e_mail = 'nicolasamato@outlook.com', cantidad_de_personas = 12)
   pedido2 = haga_su_pedido(nombre = 'maru', e_mail = 'maradelbianco@hotmail.com', cantidad_de_personas = 15)
   return render(request, 'haga_su_pedido.html' ,{'haga_su_pedido':[pedido1, pedido2]})



def mostrar_tipo_de_postre(request):
  pedido_postre = tipo_de_postre(cantidad_de_personas = 12, nombre_torta = 'copitos', relleno = 'chocolate y dulcedeleche' )
  return render(request, 'tipo_de_postre.html' ,{'tipo_de_postre':[pedido_postre]})


  
def mostrar_tipo_de_relleno(request):
   pedido_relleno = tipo_de_relleno(relleno = 'chocolate y dulcedeleche', crocante = 'mani', numero_de_pisos = 3 )
   return render(request, 'tipo_de_relleno.html' ,{'tipo_de_relleno':[pedido_relleno]})