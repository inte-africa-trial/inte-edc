from django.db import models
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from edc_model.models import BaseUuidModel


class Anthropometry(CrfModelMixin, BaseUuidModel):
    weight = edc_models.WeightField()

    height = edc_models.HeightField()

    bmi = models.DecimalField(
        verbose_name="BMI",
        decimal_places=1,
        max_digits=7,
        help_text="kg/mm^2 (Note: this field is read only. The value is calculated)",
    )

    waist_circumference = edc_models.WaistCircumferenceField()

    sys_blood_pressure_r1 = edc_models.SystolicPressureField(null=True, blank=False,)

    dia_blood_pressure_r1 = edc_models.DiastolicPressureField(null=True, blank=False,)

    sys_blood_pressure_r2 = edc_models.SystolicPressureField(null=True, blank=False,)

    dia_blood_pressure_r2 = edc_models.DiastolicPressureField(null=True, blank=False,)

    def save(self, *args, **kwargs):
        self.bmi = round((float(self.weight) / (float(self.height) / 100.0)), 2)
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Anthropometry"
        verbose_name_plural = "Anthropometry"
