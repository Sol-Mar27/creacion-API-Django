# Generated by Django 5.1.1 on 2024-09-06 01:50

import apps.usuarios.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_de_cuenta',
            field=models.ForeignKey(blank=True, default=apps.usuarios.models.get_default_tipo_de_cuenta, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.tipodecuenta'),
        ),
    ]
