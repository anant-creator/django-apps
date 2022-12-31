# Generated by Django 3.0.7 on 2020-09-19 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educationhub', '0004_remove_all_courses_startsfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_courses',
            name='startsfrom',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 5, 54, 24, 16601, tzinfo=utc), verbose_name='starts from'),
            preserve_default=False,
        ),
    ]
