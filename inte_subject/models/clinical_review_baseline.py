from django.db import models
from edc_constants.choices import YES_NO
from edc_model import models as edc_models
from edc_visit_schedule.constants import DAY1

from ..model_mixins import (
    CrfModelMixin,
    ClinicalReviewBaselineHivModelMixin,
    ClinicalReviewBaselineHtnModelMixin,
    ClinicalReviewBaselineDmModelMixin,
    ClinicalReviewModelMixin,
)


class ClinicalReviewBaselineError(Exception):
    pass


class ClinicalReviewBaseline(
    ClinicalReviewBaselineHivModelMixin,
    ClinicalReviewBaselineHtnModelMixin,
    ClinicalReviewBaselineDmModelMixin,
    ClinicalReviewModelMixin,
    CrfModelMixin,
    edc_models.BaseUuidModel,
):

    health_insurance = models.CharField(
        verbose_name="Does the patient have any private or work-place health insurance?",
        max_length=15,
        choices=YES_NO,
    )

    patient_club = models.CharField(
        verbose_name="Does the patient belong to a ‘club’ that supports medicines purchase?",
        max_length=15,
        choices=YES_NO,
    )

    def save(self, *args, **kwargs):
        if (
            self.subject_visit.visit_code != DAY1
            and self.subject_visit.visit_code_sequence != 0
        ):
            raise ClinicalReviewBaselineError(
                f"This model is only valid at baseline. Got `{self.subject_visit}`."
            )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Clinical Review: Baseline"
        verbose_name_plural = "Clinical Review: Baseline"
