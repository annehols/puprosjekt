# Generated by Django 2.1.7 on 2019-02-21 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meny', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenyItem',
            new_name='Item',
        ),
    ]
