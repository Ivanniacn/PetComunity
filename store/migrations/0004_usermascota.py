# Generated by Django 4.2.20 on 2025-07-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productotienda_imagen_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='userMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('contrasenia', models.CharField(max_length=20)),
            ],
        ),
    ]
