# Generated by Django 3.0.6 on 2020-06-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0024_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='img/blog/main-blog/maxx.jpg', upload_to='img/restaurant/'),
        ),
    ]
