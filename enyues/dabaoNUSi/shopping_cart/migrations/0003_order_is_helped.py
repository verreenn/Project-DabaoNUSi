# Generated by Django 3.0.6 on 2020-07-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20200708_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_helped',
            field=models.BooleanField(default=False),
        ),
    ]
