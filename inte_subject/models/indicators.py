from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NOT_REQUIRED
from edc_constants.constants import NOT_REQUIRED, YES
from edc_model import models as edc_models
from edc_model.models import BaseUuidModel
from edc_vitals import calculate_avg_bp
from edc_vitals.model_mixins import WeightHeightBmiModelMixin
from edc_vitals.models import DiastolicPressureField, SystolicPressureField

from ..model_mixins import CrfModelMixin


class Indicators(WeightHeightBmiModelMixin, CrfModelMixin, BaseUuidModel):

    lower_bmi_value = 15.0

    r1_taken = models.CharField(
        verbose_name=mark_safe("Was a blood pressure reading taken"),
        max_length=15,
        choices=YES_NO,
        default=YES,
    )

    r1_reason_not_taken = models.TextField(
        verbose_name="reason not taken", max_length=250, null=True, blank=True
    )

    sys_blood_pressure_r1 = SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r1 = DiastolicPressureField(null=True, blank=True)

    r2_taken = models.CharField(
        verbose_name=mark_safe("Was a <u>second</u> blood pressure reading taken"),
        max_length=15,
        choices=YES_NO_NOT_REQUIRED,
        default=NOT_REQUIRED,
    )

    r2_reason_not_taken = models.TextField(max_length=250, null=True, blank=True)

    sys_blood_pressure_r2 = SystolicPressureField(null=True, blank=True)

    dia_blood_pressure_r2 = DiastolicPressureField(null=True, blank=True)

    sys_blood_pressure_avg = models.IntegerField(
        verbose_name="Blood pressure: systolic (average)",
        null=True,
        blank=True,
    )

    dia_blood_pressure_avg = models.IntegerField(
        verbose_name="Blood pressure: diastolic (average)",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.sys_blood_pressure_avg, self.dia_blood_pressure_avg = calculate_avg_bp(
            sys_blood_pressure_one=self.sys_blood_pressure_r1,
            sys_blood_pressure_two=self.sys_blood_pressure_r2,
            dia_blood_pressure_one=self.dia_blood_pressure_r1,
            dia_blood_pressure_two=self.dia_blood_pressure_r2,
        )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Indicators"
        verbose_name_plural = "Indicators"
