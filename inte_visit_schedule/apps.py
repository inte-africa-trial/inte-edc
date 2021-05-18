from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "inte_visit_schedule"
    default_auto_field = "django.db.models.BigAutoField"
