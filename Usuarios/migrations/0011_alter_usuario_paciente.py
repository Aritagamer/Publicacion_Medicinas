# Generated by Django 4.0.1 on 2022-01-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0010_remove_usuario_paciente_usuario_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Paciente',
            field=models.ManyToManyField(blank=True, to='Usuarios.Usuario'),
        ),
    ]