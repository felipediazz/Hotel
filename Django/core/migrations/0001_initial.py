# Generated by Django 3.2.4 on 2021-06-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Cliente')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido Cliente')),
                ('nom_usuario', models.CharField(max_length=100, verbose_name='Nombre Usuario')),
                ('num_telefonico', models.IntegerField(verbose_name='Numero de Telefono')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo Electronico')),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
        ),
    ]