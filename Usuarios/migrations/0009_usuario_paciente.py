# Generated by Django 4.0.1 on 2022-01-24 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0008_remove_usuario_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.usuario'),
        ),
    ]
