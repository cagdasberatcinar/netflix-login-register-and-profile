# Generated by Django 4.2.8 on 2024-02-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_video_isnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='isnew',
            field=models.BooleanField(default=False, verbose_name='Yeni mi?'),
        ),
    ]
