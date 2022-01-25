from django.shortcuts import render


def Identificar_Usuario(request):
    user = request.session.get("Nombre",'')

    if request.session.get("Working_ID","") != request.session.get("User_ID",""):
        user = "%s (%s)"%(user,request.session.get("Working_Name",''))

    return (user)