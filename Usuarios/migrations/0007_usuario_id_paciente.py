# Generated by Django 4.0.1 on 2022-01-24 10:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_remove_usuario_id_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ID_Paciente',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
