from django.urls import path
from MiApp.views import mostrar_pedido, mostrar_tipo_de_postre, mostrar_tipo_de_relleno, mostrar_index, nuevo_pedido 
from MiApp.forms import haga_su_pedidoForm, tipo_de_postreForm, tipo_de_rellenoForm


urlpatterns = [
    path('mostrar_index/', mostrar_index),
    path('mostrar_pedido/', mostrar_pedido, name='Pedido'),
    path('nuevo_pedido/', nuevo_pedido, name='Pedido Nuevo'),
    path('mostrar_tipo_de_postre/', mostrar_tipo_de_postre, name='Postre'),
    path('mostrar_tipo_de_relleno/', mostrar_tipo_de_relleno, name='Relleno'),
    path('haga_su_pedidoForm/', haga_su_pedidoForm),
    path('tipo_de_postreForm/', tipo_de_postreForm),
    path('tipo_de_rellenoForm/', tipo_de_rellenoForm),
]