from django.db import models
from Usuarios.models import Usuario

# Create your models here.
class Medicinas(models.Model):
    Medicamento = models.CharField(verbose_name='Medicamento',null=False,blank=False,max_length=100)
    Unidades = models.FloatField(verbose_name="Cantidad",null=True,blank=True)
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Medicamento

    class Meta:
        ordering = ['Medicamento']
        verbose_name = "Medicina"
        verbose_name_plural = "Medicinas"