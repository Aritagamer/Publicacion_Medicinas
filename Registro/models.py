from django.db import models
from Usuarios.models import Usuario
from Inventario.models import Medicinas
# Create your models here.
class Registro(models.Model):
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha_Hora = models.DateTimeField(verbose_name="Hora",null=False,blank=False,auto_now_add=True)
    Medicamento = models.ForeignKey(Medicinas,on_delete=models.SET_NULL,null=True)
    Dosis = models.FloatField(verbose_name="Dosis",null=False,blank=False)

    def __str__(self):
        return self.Fecha_Hora

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"