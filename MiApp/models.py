from django.db import models

# Create your models here.

class haga_su_pedido(models.Model):
    nombre = models.CharField(max_length = 40)
    e_mail = models.EmailField()
    cantidad_de_personas = models.IntegerField()


class tipo_de_postre(models.Model):
    cantidad_de_personas = models.IntegerField()
    nombre_torta = models.CharField(max_length = 40)
    relleno = models.CharField(max_length = 40)


class tipo_de_relleno(models.Model):
    relleno = models.CharField(max_length = 40)
    crocante = models.CharField(max_length = 40)
    numero_de_pisos = models.IntegerField()

class