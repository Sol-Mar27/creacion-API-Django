# Generated by Django 5.1.1 on 2024-09-06 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_idioma_codigo_alter_idioma_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_de_cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.tipodecuenta'),
        ),
    ]
