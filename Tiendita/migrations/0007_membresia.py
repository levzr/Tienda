# Generated by Django 5.0.1 on 2024-02-26 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiendita', '0006_delete_contenidoeducativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id_membresia', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tiendita.cliente')),
            ],
        ),
    ]
