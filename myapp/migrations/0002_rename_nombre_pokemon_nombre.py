# Generated by Django 4.1.6 on 2023-02-08 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]