# Generated by Django 4.2.3 on 2023-08-04 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitio',
            old_name='nombre_encargado',
            new_name='nombre_director',
        ),
    ]
