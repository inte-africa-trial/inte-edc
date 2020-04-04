from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_lab.choices import RESULT_QUANTIFIER
from edc_lab.constants import EQ

from ..choices import GLUCOSE_UNITS


class GlucoseTestModelMixin(models.Model):
    fasted = models.CharField(
        verbose_name="Has the participant fasted?",
        max_length=15,
        choices=YES_NO,
        null=True,
        blank=False,
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
        blank=True,
        null=True,
    )

    glucose_datetime = models.DateTimeField(
        verbose_name=mark_safe("<u>Time</u> glucose <u>level</u> measured"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
