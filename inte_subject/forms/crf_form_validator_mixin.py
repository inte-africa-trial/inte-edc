from django.apps import apps as django_apps
from edc_utils import age


class CrfFormValidatorMixin:

    consent_model_cls = "inte_consent.subjectconsent"
    screening_model_cls = "inte_screening.subjectscreening"

    @property
    def age_in_years(self):
        return age(self.subject_consent.dob, self.report_datetime).years

    @property
    def subject_screening(self):
        subject_screening_model_cls = django_apps.get_model(self.screening_model_cls)
        return subject_screening_model_cls.objects.get(
            subject_identifier=self.subject_identifier
        )

    @property
    def primary_enrolment_clinic_type(self):
        return self.subject_screening.clinic_type

    @property
    def subject_identifier(self):
        try:
            subject_identifier = self.instance.subject_visit.subject_idenfifier
        except AttributeError:
            subject_identifier = self.cleaned_data.get(
                "subject_visit"
            ).subject_identifier
        return subject_identifier

    @property
    def subject_consent(self):
        subject_consent_model_cls = django_apps.get_model(self.consent_model_cls)
        return subject_consent_model_cls.objects.get(
            subject_identifier=self.subject_identifier
        )

    @property
    def report_datetime(self):
        return self.cleaned_data.get("subject_visit").report_datetime
