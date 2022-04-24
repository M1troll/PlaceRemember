from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime, timedelta, timezone
from django.utils.timesince import timesince


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image_url = models.CharField(max_length=100, null=True, default='/static/images/base_avatar.png', verbose_name="Фото")

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Impression(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название места")
    description = models.TextField(verbose_name="Описание")

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    lon = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Впечатление'
        verbose_name_plural = 'Впечатления'
