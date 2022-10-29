# Generated by Django 3.2.15 on 2022-10-26 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20221025_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название мероприятия')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
                ('video_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
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