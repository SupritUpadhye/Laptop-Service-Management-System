# Generated by Django 5.0.6 on 2024-06-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_team_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='serviceDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
