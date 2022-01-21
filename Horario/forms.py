from django import forms

class Set_Horario(forms.Form):
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
    Medicamento = forms.CharField(label="Medicamento",required=True, widget=forms.Select(attrs={'class' : 'form-select', "style":"width: 50vw; font-size: 2.5vh;"}))
    Dosis  = forms.FloatField(min_value=0, label="Dosis",localize=False,widget=forms.NumberInput(attrs={'class':'form-control', "style":"width: 10vw; font-size: 2.5vh;"}))
    

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data