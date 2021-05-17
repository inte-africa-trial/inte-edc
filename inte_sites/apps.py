from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = "inte_sites"
    default_auto_field = "django.db.models.BigAutoField"
