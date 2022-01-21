from django import forms
from Registro.forms import Registro

class Set_Horario(forms.Form,Registro):
    Dia = forms.ChoiceField(label="Dia",required=True,choices=[
        [1,"Lunes"],
        [2,"Martes"],
        [3,"Miercoles"],
        [4,"Jueves"],
        [5,"Viernes"],
        [6,"Sabado"],
        [7,"Domingo"]
        ])
    Hora = forms.IntegerField(label="Hora",max_value=24,min_value=0)
    Minutos = forms.IntegerField(label="Minutos",max_value=60,min_value=0)
    

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data