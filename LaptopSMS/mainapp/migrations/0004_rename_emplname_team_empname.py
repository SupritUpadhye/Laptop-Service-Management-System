# Generated by Django 5.0.6 on 2024-06-28 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_team_delivery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='emplName',
            new_name='empName',
        ),
    ]
