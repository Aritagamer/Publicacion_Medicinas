# Generated by Django 4.0.1 on 2022-01-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Horario', '0002_alter_horario_options_rename_dia_horario_num_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='Hora',
            field=models.IntegerField(blank=True, default=0, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='Minutos',
            field=models.IntegerField(blank=0, verbose_name='Minutos'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='Num_Dia',
            field=models.IntegerField(blank=True, default=0, verbose_name='Dia de la semana'),
        ),
    ]
