# Generated by Django 4.2.10 on 2024-03-09 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0016_offlineaddress_delete_offlineadmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='offlineaddress',
            name='branchname',
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
    ]
