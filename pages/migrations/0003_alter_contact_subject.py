# Generated by Django 4.0.5 on 2022-09-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_contact_email_alter_contact_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]