# Generated by Django 4.0.5 on 2022-07-08 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_remove_guest_ticket_guest_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='pin',
            field=models.ForeignKey(max_length=6, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.pin'),
        ),
    ]