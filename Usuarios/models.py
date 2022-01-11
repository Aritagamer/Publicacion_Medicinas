from django.db import models

# Create your models here.

class Usuario (models.Model):

    Nombre = models.CharField(verbose_name="Nombre",max_length=75,null=False,blank=False)
    Password = models.CharField(verbose_name="Contraseña",max_length=110,null=False,blank=False)
    Email = models.EmailField(verbose_name="Correo",max_length=100,null=False,blank=False)
    Fecha_Nac = models.DateField(verbose_name="Fecha de Nacimiento")
    Ultimo_Inicio = models.DateTimeField(verbose_name = "Ultimo inicio",auto_now=True)



    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"