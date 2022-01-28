from django.db import models
import uuid

# Create your models here.

class Usuario (models.Model):

    Nombre = models.CharField(verbose_name="Nombre",max_length=70,null=False,blank=False)
    Password = models.CharField(verbose_name="Contraseña",max_length=110,null=False,blank=False)
    Email = models.EmailField(verbose_name="Correo",max_length=100,null=False,blank=False)
    Fecha_Nac = models.DateField(verbose_name="Fecha de Nacimiento")
    Ultimo_Inicio = models.DateTimeField(verbose_name = "Ultimo inicio",auto_now=True)
    #Paciente = models.ManyToManyField('self',blank=True)
    ID_Paciente = models.UUIDField(primary_key=False,null=False,blank=False,default=uuid.uuid4,editable=False)



    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class rel_Pacientes(models.Model):

    Cuidador = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='%(class)s_Cuidador')
    Paciente = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='%(class)s_Paciente')
    Aceptado = models.BooleanField(verbose_name="Aceptado",null=False,blank=False)

    def __str__(self):
        return self.Paciente.Nombre