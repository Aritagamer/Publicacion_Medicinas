from django import forms
from django.shortcuts import render
from .forms import Registro
from .models import Medicinas
from Usuarios.models import Usuario
from Methods.common import Identificar_Usuario as IU

# Create your views here.
def nuevo(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})

    if request.method  == "POST":
        
        formulario = Registro(request.POST)

        if not formulario.is_valid():
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        usuario  = Usuario.objects.get(id = request.session.get("Working_ID") )
        medicina = Medicinas(
            Medicamento = data.get('Medicamento'),
            Unidades = data.get('Unidades'),
            ID_Usuario = usuario,
            Registro = data.get('Registro')
        )

        medicina.save()

        return render(request,'exito.html',{"user":user,"mensaje":"Nuevo Medicamento registrado con exito",'URL':'/inv/'})

    f = Registro(auto_id=True)

    return render(request,'Formularios.html',{"user":user,"Formulario":f})

def Editar(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})

    if request.method  == "POST":
        
        formulario = Registro(request.POST)

        if not formulario.is_valid():
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        medicina = Medicinas.objects.get(id = request.session.get("Temp_ID"))
        request.session["Temp_ID"] = ''
        medicina.Medicamento = data.get("Medicamento")
        medicina.Unidades = data.get("Unidades")
        medicina.Registro = data.get("Registro")
        medicina.save()

        return render(request,'exito.html',{"user":user,"mensaje":"Medicamento actualizado con exito",'URL':'/inv/'})

    
    request.session["Temp_ID"] = request.GET.get("id")
    medicina = Medicinas.objects.get(id = request.GET.get("id"))
    
    f = Registro(auto_id=True)
    f.fields["Medicamento"].initial = medicina.Medicamento
    f.fields["Unidades"].initial = medicina.Unidades
    f.fields["Registro"].initial = medicina.Registro
    return render(request,'Formularios.html',{"user":user,"Formulario":f})


def Eliminar(request):
    user = IU(request)
    if user == '':
        return render(request,'error.html',{"user":user,'URL':'/'})
    if request.method == "POST":
        eliminado = Medicinas.objects.get( id = request.POST.get("id",""))
        eliminado.delete()
        return render(request,'exito.html',{"user":user,"mensaje":"Medicamento eliminado con exito",'URL':'/inv/'})

    return render(request,'error.html',{"user":user,"mensaje":"error inesperado",'URL':'/inv/'})


def Inventario(request):
    user = IU(request)
    id = request.session.get("Working_ID","")

    if request.method  == "POST":
        
        formulario = Registro(request.POST)

        if not formulario.is_valid():
            return render(request,'Formularios.html',{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data
        usuario  = Usuario.objects.get(id = request.session.get("Working_ID") )
        medicina = Medicinas(
            Medicamento = data.get('Medicamento'),
            Unidades = data.get('Unidades'),
            ID_Usuario = usuario,
            Registro = data.get('Registro')
        )

        medicina.save()

        return render(request,'exito.html',{"user":user,"mensaje":"Nuevo Medicamento registrado con exito",'URL':'/inv/'})


    search = Medicinas.objects.filter(ID_Usuario = id)
    f = Registro(auto_id=True)
    return render(request,'Inventario.html',{"user":user,"elem":search,"Formulario":f})