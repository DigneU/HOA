# Generated by Django 4.0.3 on 2022-04-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_booking_adults_booking_children'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='rooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0),
        ),
    ]
