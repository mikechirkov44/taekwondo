# Generated by Django 3.2.15 on 2022-09-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20220927_0751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]