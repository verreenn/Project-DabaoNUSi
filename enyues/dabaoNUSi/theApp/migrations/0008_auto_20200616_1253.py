# Generated by Django 3.0.6 on 2020-06-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0007_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='average_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]
