# Generated by Django 4.2.10 on 2024-05-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0030_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.PositiveIntegerField(help_text='Duration in months'),
        ),
    ]
