from django.urls import path, re_path
from Horario import views

urlpatterns = [
    re_path('',views.Tabla_Horario,name='vista_Horario'),
    path('new/',views.New_Horario),
    path('update/',views.Update_Horario),
    path('delete/',views.Delete_Horario),
    path('give/',views.Give_Horario)
]