# Generated by Django 3.0.6 on 2020-07-11 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_order_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.CharField(max_length=100),
        ),
    ]
