# Generated by Django 3.0.6 on 2020-06-16 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0008_auto_20200616_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='average_price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='average_rating',
        ),
    ]
