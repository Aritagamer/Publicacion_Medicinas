from django import forms

class Registro(forms.Form):
    Medicamento = forms.CharField(required=True,max_length=95,label="Nombre del medicamento",widget=forms.TextInput(attrs={'class':'form-control'}))
    Unidades  = forms.FloatField(min_value=1, label="Cantidad",localize=False,widget=forms.NumberInput(attrs={'class':'form-control'}))

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data