from django.db import models
# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    full_text = models.TextField('Обращение')
    category = models.TextField('Категория')
    theme = models.TextField('Тема')

    class Status(models.TextChoices):
        CREATED = 'CR', _('Created')
        ACCEPTED = 'AC', _('Accepted')
        REJECTED = 'RE', _('Rejected')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.CREATED,
    )

    def __str__(self):
        return self.full_text

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
