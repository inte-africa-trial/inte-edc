from django.apps import AppConfig as DjangoApponfig
from django.conf import settings
from django.db.backends.signals import connection_created
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_utils.sqlite import activate_foreign_keys


class AppConfig(DjangoApponfig):
    name = "inte_screening"
    verbose_name = "INTE: Screening"
    screening_age_adult_upper = 99
    screening_age_adult_lower = 18
    include_in_administration_section = True
    has_exportable_data = True

    def ready(self):
        connection_created.connect(activate_foreign_keys)
