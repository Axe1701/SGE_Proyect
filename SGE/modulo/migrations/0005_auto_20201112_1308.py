# Generated by Django 3.1.2 on 2020-11-12 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo', '0004_auto_20201112_1231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actividades',
            new_name='Actividade',
        ),
        migrations.RenameModel(
            old_name='Ambientes',
            new_name='Ambiente',
        ),
        migrations.RenameModel(
            old_name='SubEventos',
            new_name='SubEvento',
        ),
    ]
