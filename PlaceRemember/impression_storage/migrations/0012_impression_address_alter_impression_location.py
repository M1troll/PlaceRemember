# Generated by Django 4.0.4 on 2022-04-28 18:36

from django.db import migrations, models
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('impression_storage', '0011_alter_impression_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='impression',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='impression',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
        ),
    ]
