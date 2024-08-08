# Generated by Django 4.2.10 on 2024-03-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nipracademy', '0018_alter_payment_order_id_alter_payment_payment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
                ('faculty_image', models.ImageField(blank=True, upload_to='media/Faculty_img', verbose_name='Faculty')),
            ],
        ),
    ]