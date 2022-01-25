from django import forms
from .models import Usuario
from werkzeug.security import generate_password_hash,check_password_hash

class registro(forms.Form):

    Email = forms.EmailField(label="Correo",required=True,max_length=100,widget=forms.EmailInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))
    Password = forms.CharField(label="Contraseña",required=True,max_length=55,widget=forms.PasswordInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))

    error_css_class = 'alert alert-danger'

    def clean(self):
        cd = self.cleaned_data
        try:

            usuario = Usuario.objects.get(Email = cd.get('Email'))

        except Usuario.DoesNotExist:

            self.add_error('Email', "Correo electronico no registrado")
            return cd

        if not check_password_hash(usuario.Password,cd.get('Password')):
            self.add_error('Password', "La contraseña no es correcta")
        return cd

class Personal_Info(forms.Form):
    
    Email = forms.EmailField(label="Correo",required=True,max_length=100,widget=forms.EmailInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))
    Password = forms.CharField(label="Contraseña",required=True,max_length=55,widget=forms.PasswordInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))
    Confirm_Password = forms.CharField(label="Confirme la contraseña",required=True,max_length=55,widget=forms.PasswordInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))
    Nombre = forms.CharField(label="Nombre",max_length=75,required=True,widget=forms.TextInput(attrs={'class':'form-control', "style":"width: 50vw; font-size: 2.5vh;"}))
    Fecha_Nac = forms.DateField(label="Fecha de Nacimiento",input_formats=('%d/%m/%Y','%d/%m/%y','%Y-%m-%d'),widget=forms.DateInput(attrs={'class':'form-control',"type" : "date", "style":"width: 50vw; font-size: 2.5vh;"}))

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        cd = self.cleaned_data
        if cd.get('Password') != cd.get('Confirm_Password'):
            self.add_error('Confirm_Password', "Las contraseñas no coinciden")
        usuario = Usuario.objects.filter(Email = cd.get('Email'))

        if usuario:
            self.add_error('Email', "Correo electronico ya registrado")
        return cd

class reg_Paciente(forms.Form):
    ID_Paciente  = forms.CharField(label = "Id del paciente",help_text="Esta informacion la puedes encontrar en su perfil",max_length=36,required=True)  

    error_css_class = 'alert alert-danger'
    #required_css_class = 'alert alert-warning'

    def clean(self):
        return self.cleaned_data
        
    