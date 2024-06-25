# Generated by Django 5.0.6 on 2024-06-20 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('sub_monto', models.DecimalField(decimal_places=2, max_digits=20)),
                ('monto_general', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.cliente', to_field='cedula')),
                ('iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.opciones', to_field='valor_iva')),
            ],
        ),
    ]
