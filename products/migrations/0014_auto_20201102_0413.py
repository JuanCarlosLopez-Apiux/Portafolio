# Generated by Django 3.1.2 on 2020-11-02 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20201023_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='id_comuna',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='tamaño_de_departamento',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='region',
            name='id_region',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
