# Generated by Django 3.2.15 on 2022-11-07 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_auto_20221107_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='halloffameimages',
            old_name='HallOfFame',
            new_name='halloffame',
        ),
    ]