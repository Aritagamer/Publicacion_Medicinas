from django import forms
from Inventario.models import Medicinas

class Dar_medicamento(forms.Form):
    Medicamento = forms.CharField(label="Medicamento",required=True, widget=forms.Select(attrs={'class' : 'form-select'}))
    Dosis  = forms.FloatField(min_value=0, label="Dosis",localize=False,widget=forms.NumberInput(attrs={'class':'form-control'}))

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data