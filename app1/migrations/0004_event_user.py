# Generated by Django 3.1.5 on 2021-01-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210129_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
