# Generated by Django 5.0.6 on 2024-06-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('disponible', models.IntegerField(null=True)),
                ('categoria', models.CharField(choices=[('1', 'Unidad'), ('2', 'Kilo'), ('3', 'Litro'), ('4', 'Otros')], max_length=20)),
                ('tiene_iva', models.BooleanField(null=True)),
            ],
        ),
    ]