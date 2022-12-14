# Generated by Django 3.2.15 on 2022-10-27 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20221027_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_agreed',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='coach_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.coach', verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.hall', verbose_name='Залы'),
        ),
    ]
