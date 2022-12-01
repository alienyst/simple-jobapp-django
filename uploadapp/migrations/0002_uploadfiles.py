# Generated by Django 4.1.2 on 2022-11-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]