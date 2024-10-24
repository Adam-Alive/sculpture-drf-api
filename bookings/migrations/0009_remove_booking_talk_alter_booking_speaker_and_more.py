# Generated by Django 4.2 on 2024-10-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_booking_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='talk',
        ),
        migrations.AlterField(
            model_name='booking',
            name='speaker',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
