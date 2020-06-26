from django.db import models
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from inte_subject.choices import HYPERTENSION_MANAGEMENT

from ..model_mixins import CrfModelMixin


class HypertensionReview(CrfModelMixin, edc_models.BaseUuidModel):

    test_date = models.DateField(
        verbose_name="Date tested for Hypertension", null=True, blank=True,
    )

    dx = models.CharField(
        verbose_name="Has the patient been diagnosed with Hypertension?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    sys_blood_pressure = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure = edc_models.DiastolicPressureField(null=True, blank=True)

    managed_by = models.CharField(
        verbose_name="If diagnosed, how will this be managed in the next month or so?",
        max_length=25,
        choices=HYPERTENSION_MANAGEMENT,
        default=NOT_APPLICABLE,
    )

    care_start_date = models.DateField(
        verbose_name="Date clinical management started", null=True, blank=False,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Hypertension Review"
        verbose_name_plural = "Hypertension Review"
