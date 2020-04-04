from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE, NOT_ESTIMATED
from edc_model import models as edc_models


class ReviewModelMixin(models.Model):

    diagnosis_date_estimated = edc_models.IsDateEstimatedFieldNa(
        verbose_name="Is the diagnosis date estimated",
        default=NOT_ESTIMATED,
        null=True,
        blank=True,
    )

    treatment_start_date = models.DateField(
        verbose_name="When was the patient started on medicine?", null=True, blank=True,
    )

    treatment_start_date_estimated = edc_models.IsDateEstimatedFieldNa(
        verbose_name="Is the start date estimated",
        default=NOT_APPLICABLE,
        null=True,
        blank=True,
    )

    on_treatment = models.CharField(
        verbose_name="Is the patient currently taking medicines for control?",
        max_length=15,
        choices=YES_NO,
    )

    class Meta:
        abstract = True
