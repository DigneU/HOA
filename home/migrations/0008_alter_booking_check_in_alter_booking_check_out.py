# Generated by Django 4.0.3 on 2022-04-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_booking_rooms_alter_booking_adults_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
    ]