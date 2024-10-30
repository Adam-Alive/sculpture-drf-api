# Generated by Django 4.2 on 2024-10-30 21:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0011_alter_booking_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('owner', 'title')},
        ),
    ]
