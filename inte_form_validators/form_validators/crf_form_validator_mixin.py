from django.apps import apps as django_apps
from inte_screening.constants import NCD_CLINIC, HIV_CLINIC


class CrfFormValidatorMixin:
    @property
    def subject_screening(self):
        SubjectScreening = django_apps.get_model("inte_screening.subjectscreening")
        return SubjectScreening.objects.get(subject_identifier=self.subject_identifier)

    @property
    def ncd_clinic(self):
        return self.subject_screening.clinic_type == NCD_CLINIC

    @property
    def hiv_clinic(self):
        return self.subject_screening.clinic_type == HIV_CLINIC

    @property
    def subject_identifier(self):
        try:
            subject_identifier = self.instance.subject_visit.subject_idenfifier
        except AttributeError:
            subject_identifier = self.cleaned_data.get(
                "subject_visit"
            ).subject_identifier
        return subject_identifier
