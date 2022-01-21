from django.shortcuts import render
from .forms import Set_Horario
import datetime

#__________________Importacion de modelos______________________________
from Usuarios.models import Usuario
from Horario.models import Horario
from Inventario.models import Medicinas
from Registro.models import Registro

#_________________________Create your views here._____________________
def Horario(request):
    user = request.session.get("Nombre",'')
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})

    medicinas = Medicinas.objects.filter(ID_Usuario = request.session.get("User_ID"))
    lista = [[int(i.id),i.Medicamento] for i in medicinas]
    
    if request.method  == "POST":

        formulario = Set_Horario(request.POST)

        if not formulario.is_valid():
            
            formulario.fields['Medicamento'].widget.choices = lista
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        medicamento = Medicinas.objects.get( id = data.get('Medicamento') )
        usuario  = Usuario.objects.get( id = request.session.get('User_ID'))

        try:

            New_Horario = Horario(
                Num_Dia = int (data.get('Dia')),
                Hora = data.get('Hora'),
                Minutos = data.get('Minutos'),
                Medicamento = medicamento,
                Dosis = data.get('Dosis'),
                Usuario = usuario
            )
            print("Si pase")
            New_Horario.save()
        except Exception as e:
            print("\n\n\n" + str(datetime.date.today()))
            print(e)
            print("\n\n\n")
        """new_reg = Registro(
            ID_Usuario = usuario,
            Medicamento = medicamento,
            Dosis = data.get('Dosis')
        )
        new_reg.save()"""

        return render(request,'exito.html',{"user":user,"mensaje":"Horario registrado con exito",'URL':'/hor/'})

    f = Set_Horario(auto_id=True)
    
    f.fields['Medicamento'].widget.choices = lista

    return render(request,'Formularios.html',{"user":user,"Formulario":f})

    