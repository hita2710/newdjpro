# Generated by Django 4.0 on 2021-12-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_filedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedetails',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='filedetails',
            name='filesize',
        ),
    ]
