# Generated by Django 3.0.6 on 2020-08-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
    ]
