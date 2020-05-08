from django.utils import timezone
from django.db import models


class Product(models.Model):
    """Модель товара"""
    class Meta:
        ordering = ['title']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    UNIT_POINTS = (
        ('1', 'шт.'),
        ('2', 'ком-т'),
        ('3', 'уп.')
    )

    title = models.CharField(verbose_name='Название продукта', max_length=300, blank=True)
    receipt_date = models.DateField(verbose_name='Дата поступления', default=timezone.now, blank=True)
    price = models.PositiveIntegerField(verbose_name='Стоимость', blank=True)
    unit = models.CharField('Единица измерения', choices=UNIT_POINTS, max_length=10, blank=True)
    provider_name = models.CharField(verbose_name='Имя поставщика', max_length=300, blank=True)

    def __str__(self):
        return f'title: {self.title}, price: {self.price} by {dict(self.UNIT_POINTS)[self.unit]}'


