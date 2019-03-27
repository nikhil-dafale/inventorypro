# Generated by Django 2.0 on 2019-03-23 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='composites',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='metals',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='plastics',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
