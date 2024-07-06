# Generated by Django 5.0.6 on 2024-07-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_user_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('monthly_revenue', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
