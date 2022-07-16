# Generated by Django 4.0.5 on 2022-07-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_remove_choices_description_choices_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='user_drink',
        ),
        migrations.AddField(
            model_name='drink',
            name='title',
            field=models.CharField(choices=[('More Beer', 'More Beer'), ('Bottle Water', 'Bottle Water'), ('Malk', 'Malk'), ('Coke', 'Coke'), ('Wine', 'Wine')], default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
