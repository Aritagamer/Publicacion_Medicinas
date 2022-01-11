from django.urls import path
from Usuarios import views

urlpatterns = [
    path('sign_up/',views.Registrarse),
    path('sign_in/',views.Iniciar),
    path('logged/',views.Iniciado),
    path('log_out/',views.Salir)
]
