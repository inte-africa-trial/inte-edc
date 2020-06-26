from django.db import models
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from ..model_mixins import CrfModelMixin


class HivReview(CrfModelMixin, edc_models.BaseUuidModel):

    test_date = models.DateField(
        verbose_name="Date tested for HIV", null=True, blank=True,
    )

    dx = models.CharField(
        verbose_name="Has the patient been infected with HIV?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    care_start_date = models.DateField(
        verbose_name="Date ART started", null=True, blank=False,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "HIV Review"
        verbose_name_plural = "HIV Review"
