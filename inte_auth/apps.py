from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = "inte_auth"
    verbose_name = "INTE Authentication and Permissions"
