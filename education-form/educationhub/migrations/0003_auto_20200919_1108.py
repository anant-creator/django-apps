# Generated by Django 3.0.7 on 2020-09-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationhub', '0002_auto_20200919_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_courses',
            name='startsfrom',
            field=models.DateTimeField(verbose_name='starts from'),
        ),
    ]
