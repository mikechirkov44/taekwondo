# Generated by Django 3.2.15 on 2022-10-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_calendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='in_archive',
            field=models.BooleanField(default=False, verbose_name='В архиве'),
        ),
    ]
