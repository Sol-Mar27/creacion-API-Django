# Generated by Django 5.1.1 on 2024-09-10 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_alter_evento_tipo_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='hora_apertura',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_cierre',
            field=models.TimeField(),
        ),
    ]
