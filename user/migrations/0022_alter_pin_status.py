# Generated by Django 4.0.5 on 2022-06-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_remove_ticket_status_pin_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='status',
            field=models.CharField(default='Not Activated', max_length=20),
        ),
    ]