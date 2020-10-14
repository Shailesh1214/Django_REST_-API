# Generated by Django 3.1.2 on 2020-10-14 21:03

import HRM.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=HRM.models.Users.upload_photo),
        ),
        migrations.AlterField(
            model_name='users',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to=HRM.models.Users.upload_file),
        ),
    ]
