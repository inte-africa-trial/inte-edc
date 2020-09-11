from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NOT_REQUIRED
from edc_constants.constants import NOT_REQUIRED, YES
from edc_model import models as edc_models
from edc_model.models import BaseUuidModel

from django.core.validators import MaxValueValidator, MinValueValidator
from ..model_mixins import CrfModelMixin


class Indicators(CrfModelMixin, BaseUuidModel):
    weight = edc_models.WeightField(
        validators=[MinValueValidator(25), MaxValueValidator(200)],
        null=True,
        blank=True,
    )

    height = edc_models.HeightField(null=True, blank=True,)

    r1_taken = models.CharField(
        verbose_name=mark_safe("Was a blood pressure reading taken"),
        max_length=15,
        choices=YES_NO,
        default=YES,
    )

    r1_reason_not_taken = models.TextField(
        verbose_name="reason not taken", max_length=250, null=True, blank=True
    )

    sys_blood_pressure_r1 = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r1 = edc_models.DiastolicPressureField(null=True, blank=True)

    r2_taken = models.CharField(
        verbose_name=mark_safe("Was a <u>second</u> blood pressure reading taken"),
        max_length=15,
        choices=YES_NO_NOT_REQUIRED,
        default=NOT_REQUIRED,
    )

    r2_reason_not_taken = models.TextField(max_length=250, null=True, blank=True)

    sys_blood_pressure_r2 = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r2 = edc_models.DiastolicPressureField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Indicators"
        verbose_name_plural = "Indicators"
