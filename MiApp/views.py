from django.shortcuts import render
from django.http import HttpResponse
from .models import haga_su_pedido, tipo_de_postre, tipo_de_relleno
from .forms import haga_su_pedidoForm, tipo_de_postreForm, tipo_de_rellenoForm


def mostrar_index(request):
   return render(request, 'index.html')

def mostrar_pedido(request):

   pedido1 = haga_su_pedido( nombre=['nombre'], e_mail=['e_mail'] , cantidad_de_personas=['cantidad_de_personas'])
   
   return render(request, 'consulta_pedido.html' ,{'haga_su_pedido':[pedido1]})


#otra opcion de def nuevo_pedido#
#def nuevo_pedido(request):
   if request.method == 'POST':          
      nue_pedido = haga_su_pedido(nombre=request.POST['nombre'], e_mai=request.POST['e_mai'])
      nue_pedido.save()
      return render(request, 'tipo_de_postre.html')
   return render(request, 'crear_nuevo_pedido.html')

def nuevo_pedido(request):
   if request.method == 'POST':
      
      formulario_PN = haga_su_pedidoForm(request.POST)
      
      if formulario_PN.is_valid():
         
         formulario_PN_limpio = formulario_PN.cleaned_data
         
         nuevo_pedido = haga_su_pedido(nombre=formulario_PN_limpio['nombre'], e_mai=formulario_PN_limpio['e_mai'])
         
         nuevo_pedido.save()
         
         return render(request, 'tipo_de_postre.html')

   else:
      formulario_PN = haga_su_pedidoForm()
      
   return render(request, 'crear_nuevo_pedido.html', {'formulario_PN': formulario_PN})

def mostrar_tipo_de_postre(request):
   
   if request.method == 'POST':
      
      formulario_npostre = tipo_de_postreForm(request.POST)
      
      if formulario_npostre.is_valid():
         
         formulario_npostre = formulario_npostre.cleaned_data
         
         pedido_postre = tipo_de_postre(cantidad_de_personas=formulario_npostre['cantidad_de_personas'], nombre_torta=formulario_npostre['nombre_torta'], relleno=formulario_npostre['relleno'])
         
         pedido_postre.save()       
          
      return render(request, 'tipo_de_relleno.html')
   
   else:
      formulario_npostre = tipo_de_postreForm
   
   return render(request, 'tipo_de_postre.html')

def mostrar_tipo_de_relleno(request):
   
   if request.method == 'POST':
      
      formulario_nrelleno = tipo_de_rellenoForm(request.POST)
      
      if formulario_nrelleno.is_valid():
         
         formulario_nrelleno = formulario_nrelleno.cleaned_data
         
         pedido_relleno = tipo_de_relleno(relleno=formulario_nrelleno['relleno'], crocante=formulario_nrelleno['crocante'], numero_de_pisos=formulario_nrelleno['numero_de_pisos'])
         
         pedido_relleno.save()   
              
         return render(request, 'index.html')
      
   else:
      formulario_nrelleno = tipo_de_rellenoForm()
   
   return render(request, 'tipo_de_relleno.html')

