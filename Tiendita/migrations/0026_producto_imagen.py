# Generated by Django 5.0.1 on 2024-04-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tiendita', '0025_transaccion_estado_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tienda'),
        ),
    ]
