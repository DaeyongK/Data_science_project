# Generated by Django 3.0.8 on 2020-12-31 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Science_Web_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryfile',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
