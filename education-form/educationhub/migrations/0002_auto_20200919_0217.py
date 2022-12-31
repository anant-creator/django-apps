# Generated by Django 3.0.7 on 2020-09-18 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educationhub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='il',
            new_name='ct',
        ),
        migrations.RemoveField(
            model_name='details',
            name='sp',
        ),
        migrations.AddField(
            model_name='all_courses',
            name='startsfrom',
            field=models.DateField(default=datetime.datetime(2020, 9, 18, 20, 47, 11, 498058, tzinfo=utc), verbose_name='starts from'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='your_choice',
            field=models.BooleanField(default=False),
        ),
    ]
