# Generated by Django 3.0.4 on 2020-06-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0009_auto_20200616_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
