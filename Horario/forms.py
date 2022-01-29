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
        ],widget=forms.Select(attrs={'class' : 'form-select texto '}))
    Opc_Hora  = forms.ChoiceField(label = "Tipo de horario",initial=24,required=True,choices=[
        [24,"Esta hora"],
        [12,"Cada 12 horas"],
        [8,"Cada 8 horas"],
        [6,"Cada 6 horas"],
        [4,"Cada 4 horas"],
        [2,"Cada 2 horas"],
        [1,"Cada hora"]
        ],
        widget=forms.RadioSelect(attrs={'class' : 'form-check-input texto '}))
    Hora = forms.IntegerField(label="Hora",max_value=24,min_value=0,widget=forms.NumberInput(attrs={'class':'texto form-control ', 'pattern':'[0-2][0-9]','placeholder':'00'}))
    Minutos = forms.IntegerField(label="Minutos",max_value=60,min_value=0,widget=forms.NumberInput(attrs={'class':'form-control  texto', 'pattern':'[0-6][0-9]','placeholder':'00'}))
    Medicamento = forms.CharField(label="Medicamento",required=True, widget=forms.Select(attrs={'class' : 'form-select texto '}))
    Dosis  = forms.FloatField(min_value=0, label="Dosis",localize=False,widget=forms.NumberInput(attrs={'class':'form-control texto '}))
    

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data

    def hidden_fields(self):
        return self.fields["Opc_Hora"]
        