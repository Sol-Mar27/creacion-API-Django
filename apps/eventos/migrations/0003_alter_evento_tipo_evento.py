# Generated by Django 5.1.1 on 2024-09-06 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_remove_tipoevento_precio_evento_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo_evento',
            field=models.ForeignKey(default='Daro', on_delete=django.db.models.deletion.SET_DEFAULT, to='eventos.tipoevento'),
        ),
    ]
