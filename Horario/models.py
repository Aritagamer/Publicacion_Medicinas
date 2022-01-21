from statistics import mode
from django.db import models
from Inventario.models import Medicinas
from Usuarios.models import Usuario
from Registro.models import Registro

# Create your models here.
class Horario (models.Model):
    Num_Dia = models.IntegerField(verbose_name="Dia de la semana",blank=True,null=False,default=0)
    Hora = models.IntegerField(verbose_name="Hora",blank=True,null=False,default=00)
    Minutos = models.IntegerField(verbose_name="Minutos",blank=00)
    Medicamento = models.ForeignKey(Medicinas,on_delete=models.CASCADE)
    Dosis = models.FloatField(verbose_name="Dosis",null=False,blank=False)
    Usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.Medicamento

    class Meta:
        ordering = ['Num_Dia','Hora','Minutos']
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"




#class Dia