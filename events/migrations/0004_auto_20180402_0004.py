# Generated by Django 2.0.3 on 2018-04-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180401_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organiser',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.SlugField(blank=True, max_length=32),
        ),
    ]
