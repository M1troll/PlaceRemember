from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Никнейм")
    image = models.ImageField(verbose_name="Фото")


class Impression(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название места")
    description = models.TextField(verbose_name="Описание")

    lon = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    author = models.ForeignKey(User, on_delete=models.CASCADE)

