from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Модель Поста
    """

    author = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Автор",
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ],
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',
        max_length=300,
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(3000),
        ],
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Описание",
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',
        max_length=3000,
    )
    is_completed = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name="Статус выполнения",
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    created = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name="Дата и время создания",
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
        auto_now=False,
        auto_now_add=False,
    )
    updated = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name="Дата и время обновления",
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = "django_api"
        ordering = ("-updated", "title")
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        if self.is_completed:
            completed = "Активно"
        else:
            completed = "Неактивно"
        return f"{self.title}({self.id}) | {self.description[0:30]}... | {completed} | {self.updated}"
