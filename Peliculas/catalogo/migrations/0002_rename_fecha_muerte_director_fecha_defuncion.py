# Generated by Django 4.2.1 on 2023-05-26 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='director',
            old_name='fecha_muerte',
            new_name='fecha_defuncion',
        ),
    ]
