# Generated by Django 4.0.1 on 2022-01-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_alter_usuario_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Usuarios.usuario'),
        ),
    ]
