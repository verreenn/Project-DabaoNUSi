# Generated by Django 3.0.6 on 2020-07-20 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_auto_20200711_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='timeEnd',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='timeStart',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
