# Generated by Django 4.2.10 on 2024-03-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0005_video_notes_video_ppt_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
