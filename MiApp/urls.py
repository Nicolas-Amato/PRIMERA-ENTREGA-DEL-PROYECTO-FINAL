from django.urls import path
from MiApp.views import mostrar_pedido, mostrar_tipo_de_postre, mostrar_tipo_de_relleno, mostrar_index, nuevo_pedido

urlpatterns = [
    path('mostrar_pedido/', mostrar_pedido, name='Pedido'),
    path('mostrar_tipo_de_postre/', mostrar_tipo_de_postre, name='Postre'),
    path('mostrar_tipo_de_relleno/', mostrar_tipo_de_relleno, name='Relleno'),
    path('mostrar_index/', mostrar_index),
    path('nuevo_pedido/', nuevo_pedido, name='Pedido Nuevo'),
    ]