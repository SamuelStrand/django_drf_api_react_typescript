from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    """
    Модель, которая содержит расширение для стандартной модели пользователя веб-платформы
    """

    user = models.OneToOneField(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Пользователь",
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
        related_name="profile",
    )
    mobile = models.CharField(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(12),
        ],
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Мобильный",
        help_text='<small class="text-muted">CharField [0, 12]</small><hr><br>',
        max_length=12,
    )
    avatar = models.ImageField(
        validators=[FileExtensionValidator(["jpg", "png"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="default/account/default_avatar.jpg",
        verbose_name="Изображение",
        help_text='<small class="text-muted"ImageField [jpg, png]</small><hr><br>',
        upload_to="uploads/admin/account/avatar",
        max_length=200,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-id",)
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.user} {self.id}"


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    if created:  # todo в первый ли раз
        try:
            Profile.objects.get_or_create(user=instance)
        except Exception as error:
            pass


class LoggingModel(models.Model):
    """
    Модель, которая содержит логирование действий и ошибок django
    """

    user = models.ForeignKey(
        db_column="user_db_column",
        db_index=True,
        db_tablespace="user_db_tablespace",
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Пользователь",
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
    )
    username = models.SlugField(
        db_column="username_db_column",
        db_index=True,
        db_tablespace="username_db_tablespace",
        error_messages=False,
        primary_key=False,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Имя пользователя",
        help_text='<small class="text-muted">SlugField [0, 300]</small><hr><br>',
        max_length=300,
        allow_unicode=False,
    )
    ip = models.GenericIPAddressField(
        db_column="ip_db_column",
        db_index=True,
        db_tablespace="ip_db_tablespace",
        error_messages=False,
        primary_key=False,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Ip адрес",
        help_text='<small class="text-muted">ip[0, 300]</small><hr><br>',
        max_length=300,
        protocol="both",
        unpack_ipv4=False,
    )
    path = models.SlugField(
        db_column="path_field_db_column",
        db_index=True,
        db_tablespace="path_field_db_tablespace",
        error_messages=False,
        primary_key=False,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Путь",
        help_text='<small class="text-muted">SlugField [0, 300]</small><hr><br>',
        max_length=300,
        allow_unicode=False,
    )
    method = models.SlugField(
        db_column="method_field_db_column",
        db_index=True,
        db_tablespace="method_field_db_tablespace",
        error_messages=False,
        primary_key=False,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(300),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Метод",
        help_text='<small class="text-muted">SlugField [0, 300]</small><hr><br>',
        max_length=300,
        allow_unicode=False,
    )
    text = models.TextField(
        db_column="text_db_column",
        db_index=True,
        db_tablespace="text_db_tablespace",
        error_messages=False,
        primary_key=False,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(3000),
        ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name="Текст ошибки/исключения/ответа",
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',
        max_length=3000,
    )
    created = models.DateTimeField(
        db_column="created_db_column",
        db_index=True,
        db_tablespace="created_db_tablespace",
        error_messages=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name="Дата и время создания",
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-created",)
        verbose_name = "Лог"
        verbose_name_plural = "Admin 5, Логи"

    def __str__(self):
        if self.username:
            try:
                username = User.objects.get(username=self.username)
            except Exception as error:
                username = ""
        else:
            username = ""
        return f"{self.created} | {username} | {self.path}"


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("name",)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date_added",)
