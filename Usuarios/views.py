import re
from django.forms import ValidationError
from django.shortcuts import render
from Methods.common import Identificar_Usuario as IU

from .forms import reg_Paciente, registro,Personal_Info,reg_Paciente

from werkzeug.security import generate_password_hash,check_password_hash

from .models import Usuario,rel_Pacientes

# Create your views here.

def Registrarse(request):
    user = IU(request)
    if request.method == "POST":
        formulario = Personal_Info(request.POST)

        if not formulario.is_valid():
            return render(request,"Formularios.html",{"user":user,"Formulario":formulario})
        usuario = Usuario(
            Nombre = formulario.cleaned_data["Nombre"],
            Password = generate_password_hash(formulario.cleaned_data["Password"]),
            Email = formulario.cleaned_data["Email"],
            Fecha_Nac = formulario.cleaned_data["Fecha_Nac"],

        )
        usuario.save()
        request.session['Nombre'] = formulario.cleaned_data["Nombre"]
        request.session['User_ID'] = usuario.id
        request.session['Working_ID'] = usuario.id
        user = formulario.cleaned_data["Nombre"]
        return render(request,"exito.html",{"user":user,'mensaje':'Nuevo usuario %s registrado correctamente'%(formulario.cleaned_data["Nombre"]),'URL':'/'})   

    f = Personal_Info(auto_id=True)
    return render(request,"Formularios.html",{"user":user,"Formulario":f})

def Iniciar(request):
    user = IU(request)

    if request.method == "POST":
        formulario = registro(request.POST)

        if not formulario.is_valid():

            return render(request,"Formularios.html",{"user":user,"Formulario":formulario})

        
        usuario = Usuario.objects.get(Email = formulario.cleaned_data['Email'])            

        user = usuario.Nombre
        request.session['Nombre'] = usuario.Nombre
        request.session['User_ID'] = str(usuario.id)
        request.session['Working_ID'] = str(usuario.id)
        usuario.save()

        return render(request,"exito.html",{
            "user":user,
            'mensaje':"Bienvenido %s inicio de sesion correcto"%(user),
            'URL':'/'
            })
    
    f = registro(auto_id=True)
    return render(request,"Formularios.html",{"user":user,"Formulario":f})

def Iniciado(request):
    user = request.session.get("Nombre",'')
    return render(request,"exito.html",{"user":user,"mensaje":"Bienvenido %s inicio de session correcto"%(user)})

def Registrado(request):
    user = request.session.get("Nombre",'')
    return render(request,"exito.html",{"user":user,"mensaje":"Nuevo usuario %s registrado correctamente"%(user)})

def Salir(request):

    request.session.flush()
    return render(request,"exito.html",{"user":'',"mensaje":"Sesion cerrada correctamente",'URL':'/'})

def Pac_Users(request):
    user = IU(request)

    if user == '':
        
        return render(request,'error.html',{"user":user,'URL':'/'})

    usuario  = Usuario.objects.get(id = request.session.get("User_ID"))

    if request.method == "POST":

        formulario = reg_Paciente(request.POST)
        if not formulario.is_valid():

            return render(request,"Formularios.html",{"user":user,"Formulario":formulario})

        data = formulario.cleaned_data

        try:

            paciente = Usuario.objects.get(ID_Paciente = data.get('ID_Paciente'))
        
        except ValidationError as e:

            return render(request,"error.html",{"user":user,"mensaje":"ID de Usuario no encontrado","url":"/users/pac/"})

        if not rel_Pacientes.objects.filter(Cuidador = usuario).filter(Paciente  = paciente):

            new_relation = rel_Pacientes(
                Cuidador = usuario,
                Paciente = paciente,
                Aceptado = False
            )

            new_relation.save()

        

        return render(request,"exito.html",{"user":user,"mensaje":"Paciente añadido con exito",'URL':'/'})
    
    usuarios = Usuario.objects.filter(id = request.session.get('User_ID',''))
    print (usuario.rel_pacientes_Cuidador.all())
    formulario = reg_Paciente(auto_id=True)
    return render(request,"Formularios.html",{"user":user,"Formulario":formulario})
    
def perfil_Users(request):
    user = request.session.get("Nombre",'')

    if user == '':
        
        return render(request,'error.html',{"user":user,'URL':'/'})

    if request.method == "POST":
        rel_ID = request.POST.get('id','')
        rechazado  = request.POST.get('none','')
        admin_ID = request.POST.get('id_admin','')
        
        if rel_ID != '':
            relacion = rel_Pacientes.objects.get(id = rel_ID)
            relacion.Aceptado = True
            relacion.save()

        elif rechazado != '':
            relacion = rel_Pacientes.objects.get(id = rechazado)
            relacion.delete()

        elif admin_ID != '':
            request.session['Working_ID'] = str(admin_ID)
            usuario_name  = Usuario.objects.get(id = admin_ID)

            request.session['Working_Name'] = usuario_name.Nombre

        
    if request.session.get("Working_ID","") != request.session.get("User_ID",""):
        user = "%s (%s)"%(request.session.get("Nombre",''),request.session.get("Working_Name",''))

    usuario  = Usuario.objects.get(id = request.session.get("User_ID"))
    
    return render(request,"Perfil.html",{"user":user,"userw":usuario,"working":int (request.session.get("Working_ID",''))})