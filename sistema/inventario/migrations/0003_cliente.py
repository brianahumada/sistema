# Generated by Django 5.0.6 on 2024-06-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=200)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20, null=True)),
                ('correo', models.CharField(max_length=100)),
                ('correo2', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
