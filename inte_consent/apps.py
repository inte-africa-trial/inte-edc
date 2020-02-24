from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "inte_consent"
    verbose_name = "INTE: Consent"
    include_in_administration_section = True
    has_exportable_data = True

    def ready(self):
        from .models.signals import (  # noqa
            subject_consent_on_post_save,  # noqa
            subject_consent_on_post_delete,  # noqa
        )  # noqa
