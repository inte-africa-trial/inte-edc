from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "inte_ae"
    verbose_name = "INTE: Adverse Events"
    include_in_administration_section = True
    has_exportable_data = True
