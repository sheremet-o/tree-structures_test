from django.db import models

import mptt


class Menu(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        verbose_name='Название'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )
    position = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Позиция'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        'self',
        related_name=u'child',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        max_length=150,
        null=False,
        verbose_name='Пункт меню'
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name


mptt.register(MenuItem,)
