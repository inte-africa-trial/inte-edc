from django.db import models
from edc_constants.choices import YES_NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models.base_uuid_model import BaseUuidModel
from inte_lists.models import DiabetesTreatment

from ..model_mixins import ReviewModelMixin, GlucoseTestModelMixin


class DiabetesInitialReview(
    ReviewModelMixin, GlucoseTestModelMixin, CrfModelMixin, BaseUuidModel
):
    diagnosis_date = models.DateField(
        verbose_name="When was the patient diagnosed with diabetes?",
    )

    treatment = models.ManyToManyField(
        DiabetesTreatment,
        verbose_name="If yes, what type of medicine is the patient currently taking?",
    )

    visual_problems = models.CharField(
        verbose_name="Has the patient experienced problems with vision linked to diabetes?",
        max_length=15,
        choices=YES_NO,
    )
    kidney_problems = models.CharField(
        verbose_name=(
            "Has the patient experienced kidney problems since diagnosed with diabetes?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    foot_ulcers = models.CharField(
        verbose_name="Has the patient experienced foot ulcers since diagnosed with diabetes?",
        max_length=15,
        choices=YES_NO,
    )

    numbness = models.CharField(
        verbose_name=(
            "Has the patient experienced numbness or burning sensation in "
            "hands or feet since diagnosed with diabetes?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    family_history = models.CharField(
        verbose_name="Is there anyone in the patient’s family with diabetes?",
        max_length=15,
        choices=YES_NO,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Diabetes Initial Review"
        verbose_name_plural = "Diabetes Initial Reviews"
