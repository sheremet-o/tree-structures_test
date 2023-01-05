from django.db import models


class MenuItem(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Пункт меню'
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    url = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_parents(self):
        if not self.parent:
            return []
        return self.parent.get_parents() + [self.parent.id]
