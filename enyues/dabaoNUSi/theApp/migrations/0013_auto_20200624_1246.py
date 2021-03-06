# Generated by Django 3.0.4 on 2020-06-24 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0012_dietary_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='prices',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='theApp.Price'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='reviews',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='theApp.Reviews'),
        ),
    ]
