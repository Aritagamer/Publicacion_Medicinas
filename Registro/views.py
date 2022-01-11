from django.shortcuts import render
from .forms import Dar_medicamento
from Inventario.models import Medicinas
from Usuarios.models import Usuario
from .models import Registro

import datetime

# Create your views here.
def Tabla_Registro(request):
    user = request.session.get("Nombre",'')
    id = request.session.get("User_ID","")

    fecha = datetime.date.today()

    if request.method == "POST":
        value = request.POST.get('search')
        if value != '':
            fecha = datetime.datetime.strptime(value,'%Y-%m-%d').date()
        

    search = Registro.objects.filter(ID_Usuario = id).filter(Fecha_Hora__date = fecha)
    return render(request,'Registros.html',{"user":user,"elem":search,"fecha":fecha})

def Dar_Medicina(request):
    user = request.session.get("Nombre",'')
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})
    medicinas = Medicinas.objects.filter(ID_Usuario = request.session.get("User_ID"))
    lista = [[int(i.id),i.Medicamento] for i in medicinas]

    if request.method  == "POST":

        formulario = Dar_medicamento(request.POST)

        if not formulario.is_valid():
            
            formulario.fields['Medicamento'].widget.choices = lista
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        medicamento = Medicinas.objects.get( id = data.get('Medicamento') )
        usuario  = Usuario.objects.get( id = request.session.get('User_ID'))

        new_reg = Registro(
            ID_Usuario = usuario,
            Medicamento = medicamento,
            Dosis = data.get('Dosis')
        )
        new_reg.save()

        return render(request,'exito.html',{"user":user,"mensaje":"Toma de medicamento registrada",'URL':'/reg/'})

    f = Dar_medicamento(auto_id=True)
    
    f.fields['Medicamento'].widget.choices = lista

    return render(request,'Formularios.html',{"user":user,"Formulario":f})