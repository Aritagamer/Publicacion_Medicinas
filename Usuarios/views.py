from django.shortcuts import render

from .forms import registro,Personal_Info

from werkzeug.security import generate_password_hash,check_password_hash

from .models import Usuario

# Create your views here.

def Registrarse(request):
    user = request.session.get("Nombre",'')
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
        user = formulario.cleaned_data["Nombre"]
        return render(request,"exito.html",{"user":user,'mensaje':'Nuevo usuario %s registrado correctamente'%(formulario.cleaned_data["Nombre"]),'URL':'/'})   

    f = Personal_Info(auto_id=True)
    return render(request,"Formularios.html",{"user":user,"Formulario":f})

def Iniciar(request):
    user = request.session.get("Nombre",'')

    if request.method == "POST":
        formulario = registro(request.POST)

        if not formulario.is_valid():

            return render(request,"Formularios.html",{"user":user,"Formulario":formulario})

        
        usuario = Usuario.objects.get(Email = formulario.cleaned_data['Email'])            

        user = usuario.Nombre
        request.session['Nombre'] = usuario.Nombre
        request.session['User_ID'] = usuario.id
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