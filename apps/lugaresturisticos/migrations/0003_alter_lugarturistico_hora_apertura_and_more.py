# Generated by Django 5.1.1 on 2024-09-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugaresturisticos', '0002_alter_lugarturistico_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugarturistico',
            name='hora_apertura',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='lugarturistico',
            name='hora_cierre',
            field=models.TimeField(),
        ),
    ]
