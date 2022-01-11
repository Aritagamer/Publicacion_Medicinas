from django.urls import path
from Registro import views

urlpatterns = [
    path('',views.Tabla_Registro),
    path('give/',views.Dar_Medicina)
]