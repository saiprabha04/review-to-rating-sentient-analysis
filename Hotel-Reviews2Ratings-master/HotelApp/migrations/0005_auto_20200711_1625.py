# Generated by Django 3.0.8 on 2020-07-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0004_auto_20200711_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
    ]
