# Generated by Django 2.0.3 on 2018-04-01 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180402_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tags',
            new_name='event_url',
        ),
    ]
