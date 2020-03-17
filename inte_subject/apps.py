from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "inte_subject"
    verbose_name = "INTE: Subject (CRFs)"
    include_in_administration_section = True
    has_exportable_data = True


102
