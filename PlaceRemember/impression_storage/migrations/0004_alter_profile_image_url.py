# Generated by Django 4.0.4 on 2022-04-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impression_storage', '0003_remove_profile_image_profile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_url',
            field=models.CharField(default='/static/images/base_avatar.png', max_length=100, null=True, verbose_name='Фото'),
        ),
    ]
