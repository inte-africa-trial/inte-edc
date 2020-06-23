from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_constants.constants import YES
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from edc_model.models import BaseUuidModel


class Indicators(CrfModelMixin, BaseUuidModel):
    weight = edc_models.WeightField()

    height = edc_models.HeightField()

    r1_taken = models.CharField(
        verbose_name=mark_safe("Was a blood pressure reading taken"),
        max_length=15,
        choices=YES_NO,
        default=YES,
    )

    sys_blood_pressure_r1 = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r1 = edc_models.DiastolicPressureField(null=True, blank=True)

    r2_taken = models.CharField(
        verbose_name=mark_safe("Was a <u>second</u> blood pressure reading taken"),
        max_length=15,
        choices=YES_NO,
        default=YES,
    )

    sys_blood_pressure_r2 = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r2 = edc_models.DiastolicPressureField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Indicators"
        verbose_name_plural = "Indicators"
