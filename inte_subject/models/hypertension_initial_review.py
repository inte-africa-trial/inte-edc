from django.db import models
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from ..choices import HYPERTENSION_MANAGEMENT
from ..model_mixins import CrfModelMixin


class HypertensionInitialReview(CrfModelMixin, edc_models.BaseUuidModel):

    dx_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient diagnosed with hypertension?",
    )

    dx_estimated_date = models.DateField(
        verbose_name="Estimated hypertension diagnoses date", null=True, editable=False,
    )

    managed_by = models.CharField(
        verbose_name="How is the patient's hypertension managed?",
        max_length=15,
        choices=HYPERTENSION_MANAGEMENT,
        default=NOT_APPLICABLE,
    )

    med_start_ago = edc_models.DurationYearMonthField(
        verbose_name=(
            "If the patient is taking medicines for hypertension, "
            "how long have they been taking these?"
        ),
        null=True,
        blank=True,
    )

    med_start_estimated_date = models.DateField(
        verbose_name="Estimated medication start date", null=True, editable=False,
    )

    def save(self, *args, **kwargs):
        if self.dx_ago:
            self.dx_estimated_date = edc_models.duration_to_date(
                self.dx_ago, self.report_datetime
            )
        if self.med_start_ago:
            self.med_start_estimated_date = edc_models.duration_to_date(
                self.med_start_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Hypertension Initial Review"
        verbose_name_plural = "Hypertension Initial Reviews"
