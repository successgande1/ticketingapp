# Generated by Django 4.0.5 on 2022-07-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_alter_pin_ticket_alter_ticket_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ticket'),
        ),
    ]
