from django.db import models
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from ..model_mixins import CrfModelMixin, ReviewModelMixin


class HivReview(ReviewModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    test_date = models.DateField(
        verbose_name="Date tested for HIV",
        null=True,
        blank=True,
        help_text="QUESTION_RETIRED",
    )

    dx = models.CharField(
        verbose_name="Has the patient been infected with HIV?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    arv_initiated = models.CharField(
        verbose_name="Has the patient started antiretroviral therapy (ART)?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="Select `not applicable` if previously reported.",
    )
    arv_initiation_actual_date = models.DateField(
        verbose_name="Date started antiretroviral therapy (ART)",
        null=True,
        blank=True,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "HIV Review"
        verbose_name_plural = "HIV Review"
