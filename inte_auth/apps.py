from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = "inte_auth"
    verbose_name = "INTE Authentication and Permissions"
    default_auto_field = "django.db.models.BigAutoField"
