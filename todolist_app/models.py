from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.utils import timezone

# Create your models here.


def _get_default_date():
    return timezone.now() + timedelta(days=1)


class ToDoList(models.Model):
    class StatusType(models.TextChoices):
        ACTIVE = 'active', _("Активно")
        DRAFT = 'draft', _("Отложено")
        DONE = 'done', _("Выполнено")

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="Автор")
    status = models.CharField("Состояние",
                              max_length=10,
                              choices=StatusType.choices,
                              default=StatusType.DRAFT)
    important = models.BooleanField("Важно",
                                    default=False)
    public = models.BooleanField("Публично",
                                 default=False)
    datetime = models.DateTimeField("Дата",
                                    default=_get_default_date())
    views = models.IntegerField("Количество просмотров", default=0)
