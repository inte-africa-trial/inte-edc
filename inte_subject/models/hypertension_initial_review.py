from django.db import models
from edc_constants.choices import YES_NO, YES_NO_DONT_KNOW
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from inte_lists.models import HypertensionTreatment

from ..model_mixins import ReviewModelMixin


class HypertensionInitialReview(ReviewModelMixin, CrfModelMixin, BaseUuidModel):
    diagnosis_date = models.DateField(
        verbose_name="When was the patient diagnosed with hypertension?"
    )

    treatment_start_date = models.DateField(null=True, blank=True)

    treatment = models.ManyToManyField(
        HypertensionTreatment,
        verbose_name="If yes, what type of medicine is the patient currently taking?",
    )

    stroke = models.CharField(
        verbose_name="Has the patient suffered a stroke in the past?",
        max_length=15,
        choices=YES_NO,
    )

    chest_pain = models.CharField(
        verbose_name="Has the patient suffered severe pain in the chest in the past?",
        max_length=15,
        choices=YES_NO,
    )

    family_history = models.CharField(
        verbose_name="Is there anyone in the patient’s family with hypertension?",
        max_length=15,
        choices=YES_NO_DONT_KNOW,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Hypertension Initial Review"
        verbose_name_plural = "Hypertension Initial Reviews"
