# Generated by Django 4.1.2 on 2022-12-17 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentification', '0006_userotp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserOTP',
        ),
    ]
