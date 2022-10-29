# Generated by Django 3.2.15 on 2022-10-27 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20221027_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='coach_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='mainapp.coach', verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='hall',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='mainapp.hall', verbose_name='Залы'),
        ),
    ]