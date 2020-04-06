from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_lab.choices import RESULT_QUANTIFIER
from edc_lab.constants import EQ

from ..choices import GLUCOSE_UNITS


class GlucoseTestModelMixin(models.Model):
    glucose_measurement_taken = models.CharField(
        verbose_name="Was a glucose measurement taken?", max_length=15, choices=YES_NO,
    )

    glucose_measurement_reason_not_taken = models.TextField(
        verbose_name="If the glucose measurement was not taken, explain?",
        max_length=250,
        null=True,
        blank=True,
    )

    fasted = models.CharField(
        verbose_name="Has the participant fasted?",
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        default=NOT_APPLICABLE,
    )

    glucose = models.DecimalField(
        verbose_name=mark_safe("Glucose <u>level</u>"),
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    glucose_quantifier = models.CharField(
        max_length=10, choices=RESULT_QUANTIFIER, default=EQ,
    )

    glucose_units = models.CharField(
        verbose_name="Units (glucose)",
        max_length=15,
        choices=GLUCOSE_UNITS,
        default=NOT_APPLICABLE,
    )

    class Meta:
        abstract = True
