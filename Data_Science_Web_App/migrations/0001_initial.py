# Generated by Django 3.0.8 on 2020-12-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('data', models.FileField(upload_to='')),
            ],
        ),
    ]
