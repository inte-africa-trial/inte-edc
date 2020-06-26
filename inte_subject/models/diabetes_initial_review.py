from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from inte_subject.choices import DIABETES_MANAGEMENT

from ..model_mixins import CrfModelMixin, GlucoseModelMixin


class DiabetesInitialReview(GlucoseModelMixin, CrfModelMixin, edc_models.BaseUuidModel):

    dx_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient diagnosed with diabetes?",
    )

    dx_estimated_date = models.DateField(
        verbose_name="Estimated diabetes diagnoses date", null=True, editable=False,
    )

    managed_by = models.CharField(
        verbose_name="How is the patient's diabetes managed?",
        max_length=25,
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
            "Has the patient had their glucose measured in the last few months?"
        ),
        max_length=15,
        choices=YES_NO,
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
