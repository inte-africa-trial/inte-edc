from django.db import models
from edc_constants.choices import YES_NO
from edc_model import models as edc_models

from ..model_mixins import (
    CrfModelMixin,
    ClinicalReviewHivModelMixin,
    ClinicalReviewHypertensionModelMixin,
    ClinicalReviewDiabetesModelMixin,
)


class ClinicalReviewBaseline(
    ClinicalReviewHivModelMixin,
    ClinicalReviewHypertensionModelMixin,
    ClinicalReviewDiabetesModelMixin,
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

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Clinical Review: Baseline"
        verbose_name_plural = "Clinical Review: Baseline"
