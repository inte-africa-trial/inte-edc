from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_lab.choices import RESULT_QUANTIFIER_NA
from edc_model import models as edc_models
from edc_model.models import date_not_future
from inte_subject.choices import DIABETES_MANAGEMENT, GLUCOSE_UNITS

from ..model_mixins import CrfModelMixin


class DiabetesInitialReview(CrfModelMixin, edc_models.BaseUuidModel):

    dx_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient diagnosed with diabetes?",
    )

    dx_estimated_date = models.DateField(
        verbose_name="Estimated diabetes diagnoses date", null=True, editable=False,
    )

    managed_by = models.CharField(
        verbose_name="How is the patient's diabetes managed?",
        max_length=15,
        choices=DIABETES_MANAGEMENT,
        default=NOT_APPLICABLE,
    )

    med_start_ago = edc_models.DurationYearMonthField(
        verbose_name=(
            "If the patient is taking medicines for diabetes, "
            "how long have they been taking these?"
        ),
        null=True,
        blank=True,
    )

    med_start_estimated_date = models.DateField(
        verbose_name="Estimated medication start date", null=True, editable=False,
    )

    glucose_performed = models.CharField(
        verbose_name=(
            "Has the patient had their fasting glucose measured in the last few months?"
        ),
        max_length=15,
        choices=YES_NO,
    )

    glucose_date = models.DateField(
        validators=[date_not_future], null=True, blank=True,
    )

    glucose = models.DecimalField(
        verbose_name=mark_safe("Fasting glucose result"),
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )

    glucose_quantifier = models.CharField(
        max_length=10, choices=RESULT_QUANTIFIER_NA, default=NOT_APPLICABLE,
    )

    glucose_units = models.CharField(
        verbose_name="Units (glucose)",
        max_length=15,
        choices=GLUCOSE_UNITS,
        default=NOT_APPLICABLE,
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
        verbose_name = "Diabetes Initial Review"
        verbose_name_plural = "Diabetes Initial Reviews"
