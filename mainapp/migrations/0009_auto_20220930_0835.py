# Generated by Django 3.2.15 on 2022-09-30 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20220927_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='coach_name',
            field=models.CharField(choices=[('1', 'Маклаков В.П.'), ('2', 'Шустова М.А.'), ('3', 'Соколов П.И.'), ('4', 'Кошкаров Б.Н.'), ('5', 'Цыварев И.В.'), ('6', 'Сер А.Р.'), ('7', 'Усачева О.А.')], max_length=200, verbose_name='ФИО тренера'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='hall',
            field=models.CharField(choices=[('1', 'С/К Спартак'), ('2', 'Ф/К Апельсин'), ('3', 'Лицей №41'), ('4', 'Гимназия №25'), ('5', 'Школа №21'), ('6', 'Школа №31'), ('7', 'Дворец Культуры'), ('8', 'Школа №37'), ('9', 'Отель "Третьяков"'), ('10', 'С/К "Синия птица"'), ('11', 'Зал единоборств')], max_length=200, verbose_name='Зал для тренировок'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки'),
        ),
    ]
