from django.urls import path
from Inventario import views

urlpatterns = [
    path('',views.Inventario),
    path('new/',views.nuevo),
    path('delete/',views.Eliminar),
    path('update/',views.Editar)
]