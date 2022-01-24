from django import forms

class Set_Horario(forms.Form):
    Dia = forms.ChoiceField(label="Dia",required=True,choices=[
        [0,"Sin Dia"],
        [1,"Lunes"],
        [2,"Martes"],
        [3,"Miercoles"],
        [4,"Jueves"],
        [5,"Viernes"],
        [6,"Sabado"],
        [7,"Domingo"],
        [8,"Diario"]
        ])
    Opc_Hora  = forms.ChoiceField(label = "Tipo de horario",required=True,choices=[
        [24,"Esta hora"],
        [12,"Cada 12 horas"],
        [8,"Cada 8 horas"],
        [6,"Cada 6 horas"],
        [4,"Cada 4 horas"],
        [2,"Cada 2 horas"],
        [1,"Cada hora"]
        ],
        widget=forms.RadioSelect())
    Hora = forms.IntegerField(label="Hora",max_value=24,min_value=0)
    Minutos = forms.IntegerField(label="Minutos",max_value=60,min_value=0)
    Medicamento = forms.CharField(label="Medicamento",required=True, widget=forms.Select(attrs={'class' : 'form-select', "style":"width: 50vw; font-size: 2.5vh;"}))
    Dosis  = forms.FloatField(min_value=0, label="Dosis",localize=False,widget=forms.NumberInput(attrs={'class':'form-control', "style":"width: 10vw; font-size: 2.5vh;"}))
    

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data