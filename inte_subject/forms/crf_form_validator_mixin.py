from django.apps import apps as django_apps


class CrfFormValidatorMixin:
    @property
    def subject_screening(self):
        subject_screening_model_cls = django_apps.get_model(
            "inte_screening.subjectscreening"
        )
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
