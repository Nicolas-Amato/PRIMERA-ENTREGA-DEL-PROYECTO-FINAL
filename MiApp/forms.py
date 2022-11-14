from django import forms

class haga_su_pedidoForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    e_mail = forms.EmailField()
    cantidad_de_personas = forms.IntegerField()
    
    
class tipo_de_postreForm(forms.Form):
    cantidad_de_personas = forms.IntegerField()
    nombre_torta = forms.CharField(max_length = 40)
    relleno = forms.CharField(max_length = 40)


class tipo_de_rellenoForm(forms.Form):
    relleno = forms.CharField(max_length = 40)
    crocante = forms.CharField(max_length = 40)
    numero_de_pisos = forms.IntegerField()