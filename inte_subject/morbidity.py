from django.core.exceptions import ObjectDoesNotExist

from .models import DiabetesInitialReview, HivInitialReview, HypertensionInitialReview


class Morbidities:
    def __init__(self, subject_identifier=None, report_datetime=None):
        self.subject_identifier = subject_identifier
        self.report_datetime = report_datetime

    @property
    def is_hypertension(self):
        return self._is_condition(HypertensionInitialReview)

    @property
    def is_hiv_pos(self):
        return self._is_condition(HivInitialReview)

    @property
    def is_diabetes(self):
        return self._is_condition(DiabetesInitialReview)

    def _is_condition(self, model_cls):
        opts = dict(subject_visit__subject_identifier=self.subject_identifier)
        if self.report_datetime:
            opts.update(subject_visit__report_datetime__lte=self.report_datetime)
        try:
            model_cls.objects.get(**opts)
        except ObjectDoesNotExist:
            return False
        return True
