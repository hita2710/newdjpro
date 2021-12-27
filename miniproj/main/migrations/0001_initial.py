# Generated by Django 4.0 on 2021-12-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mailid', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('confpassword', models.CharField(max_length=10)),
            ],
        ),
    ]
