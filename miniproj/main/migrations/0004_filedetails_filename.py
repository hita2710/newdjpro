# Generated by Django 4.0 on 2021-12-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_filedetails_filename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filedetails',
            name='filename',
            field=models.CharField(default='filename', max_length=20),
        ),
    ]
