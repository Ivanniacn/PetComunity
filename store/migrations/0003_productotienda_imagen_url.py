# Generated by Django 4.2.20 on 2025-06-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_mascota_productotienda_usuario_delete_productos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productotienda',
            name='imagen_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
