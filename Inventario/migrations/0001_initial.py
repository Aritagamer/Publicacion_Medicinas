# Generated by Django 4.0.1 on 2022-01-09 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0002_alter_usuario_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicinas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicamento', models.CharField(max_length=100, verbose_name='Medicamento')),
                ('Unidades', models.FloatField(blank=True, null=True, verbose_name='Cantidad')),
                ('ID_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
            options={
                'ordering': ['Medicamento'],
            },
        ),
    ]
