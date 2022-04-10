# Generated by Django 4.0.3 on 2022-04-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_booking_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
