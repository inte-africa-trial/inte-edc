from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = "inte_screening"
    verbose_name = "INTE: Screening"
    screening_age_adult_upper = 99
    screening_age_adult_lower = 18
    include_in_administration_section = True
    has_exportable_data = True
    default_auto_field = "django.db.models.BigAutoField"
