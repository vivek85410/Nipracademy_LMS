# Generated by Django 4.2.10 on 2024-03-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0004_alter_video_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='Notes',
            field=models.FileField(blank=True, upload_to='files/course_Notes', verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='video',
            name='ppt',
            field=models.FileField(blank=True, upload_to='files/course_ppt', verbose_name='Presentations'),
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='files/course_videos', verbose_name='Video'),
        ),
    ]