# Generated by Django 3.2.15 on 2022-10-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20221026_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.TextField(),
        ),
    ]
