# Generated by Django 4.2.8 on 2024-02-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_alter_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isnew',
            field=models.BooleanField(default=False),
        ),
    ]
