# Generated by Django 4.2.10 on 2024-03-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0013_rename_text_comment_content_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('contact', models.IntegerField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
