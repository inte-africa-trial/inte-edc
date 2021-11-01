from django.db import models
from edc_blood_results.model_mixins import (
    BloodResultsModelMixin,
    Hba1cModelMixin,
    RequisitionModelMixin,
)
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, YES
from edc_model import models as edc_models

from ..model_mixins import CrfModelMixin


class BloodResultsHba1c(
    CrfModelMixin,
    Hba1cModelMixin,
    RequisitionModelMixin,
    BloodResultsModelMixin,
    edc_models.BaseUuidModel,
):

    performed = models.CharField(
        verbose_name="Was the test performed?",
        max_length=15,
        choices=YES_NO,
        default=YES,
    )

    not_performed_reason = models.CharField(
        verbose_name="If not performed, please explain ...",
        max_length=50,
        null=True,
        blank=True,
    )

    is_poc = models.CharField(
        verbose_name="Was a point-of-care test used?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "HbA1c"
        verbose_name_plural = "HbA1c"
