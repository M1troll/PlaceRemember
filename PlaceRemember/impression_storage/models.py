from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from location_field.models.plain import PlainLocationField


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
    title = models.CharField("Название места", max_length=50)
    description = models.TextField("Описание")

    is_deleted = models.BooleanField("Удален", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    address = models.CharField('Адрес', max_length=255)
    location = PlainLocationField(based_fields=['address'], zoom=7, default='', verbose_name='Координаты')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Впечатление'
        verbose_name_plural = 'Впечатления'
