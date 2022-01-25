from django.shortcuts import render
from .forms import Set_Horario
import datetime
from Methods.common import Identificar_Usuario as IU
import Horario.func.common as vm

#__________________Importacion de modelos______________________________
from Usuarios.models import Usuario
from Horario.models import set_Horario
from Inventario.models import Medicinas
from Registro.models import Registro

#_________________________Create your views here._____________________
def Tabla_Horario(request):
    user = IU(request)

    list_dia = [' ','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})
    usuario = Usuario.objects.get(id = request.session.get("Working_ID",''))

    if request.method == 'POST':
        dia  = int (request.POST.get('dia_sel',""))
    else:
        dia = int (datetime.date.today().isoweekday())
    
    Medicamentos = set_Horario.objects.filter(Usuario = usuario)

    no_med  = Medicamentos.filter(Num_Dia = 0)
    all_med = Medicamentos.filter(Num_Dia = 8) | Medicamentos.filter(Num_Dia = dia)

    return render(request,"Horario.html",{"user":user,"elem":all_med,"dia" : list_dia[dia],"dia_index":dia,"elem_none":no_med})

def Give_Horario(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})
    
    horario  = set_Horario.objects.get(id = request.POST.get("id",""))
    
    if horario.Medicamento.Registro:
        horario.Medicamento.Unidades = float( horario.Medicamento.Unidades ) - float(horario.Dosis)
        horario.Medicamento.save()
    
    new_reg = Registro(
        ID_Usuario = horario.Usuario,
        Medicamento = horario.Medicamento,
        Dosis = horario.Dosis
    )
    new_reg.save()

    return render(request,'exito.html',{"user":user,"mensaje":"Toma de medicamento registrada",'URL':'/hor/'})
    

def New_Horario(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})

    medicinas = Medicinas.objects.filter(ID_Usuario = request.session.get("Working_ID"))
    lista = [[int(i.id),i.Medicamento] for i in medicinas]
    
    if request.method  == "POST":

        formulario = Set_Horario(request.POST)

        if not formulario.is_valid():
            
            formulario.fields['Medicamento'].widget.choices = lista
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        medicamento = Medicinas.objects.get( id = data.get('Medicamento') )
        usuario  = Usuario.objects.get( id = request.session.get('Working_ID'))

        opc = int (data.get("Opc_Hora"))

        vm.Set_Mult_Horario(hour = opc,data=data,medicamento = medicamento,usuario = usuario) 

        return render(request,'exito.html',{"user":user,"mensaje":"Horario registrado con exito",'URL':'/hor/'})

    f = Set_Horario(auto_id=True)
    
    f.fields['Medicamento'].widget.choices = lista

    return render(request,'Formularios.html',{"user":user,"Formulario":f})

def Update_Horario(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})

    medicinas = Medicinas.objects.filter(ID_Usuario = request.session.get("Working_ID"))
    lista = [[int(i.id),i.Medicamento] for i in medicinas]

    if request.method  == "POST":
        
        formulario = Set_Horario(request.POST)

        if not formulario.is_valid():
            formulario.fields['Medicamento'].widget.choices = lista
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        medicamento = Medicinas.objects.get(id = data.get('Medicamento'))
        Horario_Edit = set_Horario.objects.get(id = request.session.get("Temp_ID"))
        request.session["Temp_ID"] = ''

        Horario_Edit.Num_Dia = data.get("Dia")
        Horario_Edit.Dosis = data.get("Dosis")
        Horario_Edit.Hora = data.get("Hora")
        Horario_Edit.Minutos = data.get("Minutos")
        Horario_Edit.Hora = data.get("Hora")
        Horario_Edit.Medicamento = medicamento
        Horario_Edit.save()

        return render(request,'exito.html',{"user":user,"mensaje":"Medicamento actualizado con exito",'URL':'/hor/'})

    
    request.session["Temp_ID"] = request.GET.get("id")
    Horario_Edit = set_Horario.objects.get(id = request.GET.get("id"))
    
    f = Set_Horario(auto_id=True)
    f.fields['Medicamento'].widget.choices = lista
    f.fields["Dia"].initial = Horario_Edit.Num_Dia
    f.fields["Dosis"].initial = Horario_Edit.Dosis
    f.fields["Hora"].initial = Horario_Edit.Hora
    f.fields["Minutos"].initial = Horario_Edit.Minutos
    return render(request,'Formularios.html',{"user":user,"Formulario":f})


def Delete_Horario(request):
    user = IU(request)
    if user == '':
        
        return render(request,'error.html',{"user":user,'URL':'/'})
    
    if request.method == "POST":
        eliminado = set_Horario.objects.get( id = request.POST.get("id",""))
        eliminado.delete()
        return render(request,'exito.html',{"user":user,"mensaje":"Horario eliminado con exito",'URL':'/hor/'})

    return render(request,'error.html',{"user":user,"mensaje":"error inesperado",'URL':'/hor/'})
   