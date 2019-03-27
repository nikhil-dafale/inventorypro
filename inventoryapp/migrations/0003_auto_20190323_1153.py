# Generated by Django 2.0 on 2019-03-23 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_auto_20190323_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composites',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='metals',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='plastics',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
