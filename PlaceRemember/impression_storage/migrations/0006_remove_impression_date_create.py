# Generated by Django 4.0.4 on 2022-04-24 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impression_storage', '0005_impression_created_at_impression_date_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impression',
            name='date_create',
        ),
    ]
