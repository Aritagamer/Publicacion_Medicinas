from django.shortcuts import render


def Identificar_Usuario(request):
    user = request.session.get("Nombre",'')
    if user != '':
        return ( user)

    return (False)