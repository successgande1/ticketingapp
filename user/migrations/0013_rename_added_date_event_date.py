# Generated by Django 4.0.5 on 2022-06-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_desktop_logo_event_event_logo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='added_date',
            new_name='date',
        ),
    ]
