# Generated by Django 4.0.1 on 2022-01-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_medicinas_registro'),
        ('Usuarios', '0002_alter_usuario_password'),
        ('Horario', '0005_alter_horario_hora_alter_horario_minutos_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Horario',
            new_name='set_Horario',
        ),
    ]
