# Generated by Django 5.1.1 on 2024-09-06 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redsocial',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
