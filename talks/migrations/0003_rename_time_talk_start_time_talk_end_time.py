# Generated by Django 4.2 on 2024-09-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_alter_talk_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='talk',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]