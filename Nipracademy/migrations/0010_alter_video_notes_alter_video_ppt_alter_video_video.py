# Generated by Django 4.2.10 on 2024-03-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0009_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Notes',
            field=models.FileField(blank=True, upload_to='media/Notes_files/', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='video',
            name='ppt',
            field=models.FileField(blank=True, upload_to='media/ppt_files/', verbose_name='Presentations'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/video_files/', verbose_name='Video'),
        ),
    ]