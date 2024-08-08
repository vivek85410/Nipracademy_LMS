# Generated by Django 4.2.10 on 2024-03-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0015_alter_offlineadmission_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('contact', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='OfflineAdmission',
        ),
    ]
