from django.contrib import admin
from django_app import models


admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class ProfileAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Profile' на панели администратора
    """

    list_display = (
        "user",
        "mobile",
        "avatar",
    )
    list_display_links = (
        "user",
        "mobile",
    )
    # list_editable = (
    #     'user',
    # )
    list_filter = (
        "user",
        "mobile",
        "avatar",
    )
    # filter_horizontal = (
    #     'users',
    # )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "user",
                    "mobile",
                    "avatar",
                )
            },
        ),
    )
    search_fields = [
        "user",
        "mobile",
        "avatar",
    ]


class LoggingModelAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'LoggingModel' на панели администратора
    """

    list_display = ("username", "ip", "path", "method", "text", "created")
    list_display_links = (
        "username",
        "ip",
        "path",
        "method",
    )
    list_editable = ()
    list_filter = ("username", "ip", "path", "method", "text", "created")
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "username",
                    "ip",
                    "path",
                    "method",
                    "text",
                    "created",
                )
            },
        ),
    )
    search_fields = ["username", "ip", "path", "method", "text", "created"]


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.LoggingModel, LoggingModelAdmin)
admin.site.register(models.Room)
