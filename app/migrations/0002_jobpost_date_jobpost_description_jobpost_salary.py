# Generated by Django 4.1.2 on 2022-10-24 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 24, 16, 3, 37, 79964, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
