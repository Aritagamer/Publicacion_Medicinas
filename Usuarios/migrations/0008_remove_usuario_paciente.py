# Generated by Django 4.0.1 on 2022-01-24 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0007_usuario_id_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Paciente',
        ),
    ]