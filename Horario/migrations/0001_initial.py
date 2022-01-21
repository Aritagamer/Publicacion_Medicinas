# Generated by Django 4.0.1 on 2022-01-21 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0002_alter_usuario_password'),
        ('Inventario', '0003_medicinas_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dia', models.SmallIntegerField(blank=True, default=0, verbose_name='Dia de la semana')),
                ('Hora', models.SmallIntegerField(blank=True, default=0, verbose_name='Hora')),
                ('Minutos', models.SmallIntegerField(blank=0, verbose_name='Minutos')),
                ('Dosis', models.FloatField(verbose_name='Dosis')),
                ('Medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.medicinas')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'ordering': ['Dia', 'Hora', 'Minutos'],
            },
        ),
    ]