# Generated by Django 3.2.15 on 2022-11-07 16:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_auto_20221104_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallOfFame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('date_start', models.DateField(verbose_name='Дата начала мероприятия')),
                ('date_finish', models.DateField(verbose_name='Дата окончания мероприятия')),
            ],
            options={
                'verbose_name': 'Доски почета',
                'verbose_name_plural': 'Доска почета',
            },
        ),
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ('-date',), 'verbose_name': 'Соревнование', 'verbose_name_plural': 'Соревнования'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-date',), 'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4, 'Минимальный возраст для занятий 4 года')], verbose_name='Возраст ребенка'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='HallOfFameImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img/')),
                ('HallOfFame', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainapp.halloffame')),
            ],
            options={
                'verbose_name': 'Изображение для доски почета',
                'verbose_name_plural': 'Изображения для доски почета',
            },
        ),
    ]