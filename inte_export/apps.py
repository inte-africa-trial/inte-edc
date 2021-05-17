from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "inte_export"
    verbose_name = "INTE: Export"
    default_auto_field = "django.db.models.BigAutoField"
