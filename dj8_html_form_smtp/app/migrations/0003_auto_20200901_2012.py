# Generated by Django 3.0.6 on 2020-09-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200901_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='blood',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='dob',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
    ]
