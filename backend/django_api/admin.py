from django.contrib import admin
from django_api import models as django_models


class PostAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Post' на панели администратора
    """

    list_display = (
        "author",
        "title",
        "description",
        "is_completed",
        "created",
        "updated",
    )
    list_display_links = (
        "author",
        "title",
        "description",
    )
    list_editable = ("is_completed",)
    list_filter = (
        "author",
        "title",
        "description",
        "is_completed",
        "created",
        "updated",
    )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author",
                    "title",
                    "description",
                    "is_completed",
                    "created",
                    "updated",
                )
            },
        ),
    )
    search_fields = [
        "author",
        "title",
        "description",
        "is_completed",
        "created",
        "updated",
    ]


admin.site.register(django_models.Post, PostAdmin)
