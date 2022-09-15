from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):
    """Модель товара."""

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Введите название'
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=500,
        help_text='Введите описание модели'
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.name
