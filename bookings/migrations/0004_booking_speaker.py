# Generated by Django 4.2 on 2024-10-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_end_time_booking_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='speaker',
            field=models.CharField(default='', max_length=100),
        ),
    ]