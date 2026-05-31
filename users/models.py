from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    relative = models.CharField(
        verbose_name='Родственник',
        max_length=20,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'