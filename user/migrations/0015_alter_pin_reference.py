# Generated by Django 4.0.5 on 2022-06-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_remove_event_event_date_event_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='reference',
            field=models.UUIDField(default='984345', editable=False, primary_key=True, serialize=False),
        ),
    ]