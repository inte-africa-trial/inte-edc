from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import POS_NEG_NOTESTED, YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from ..model_mixins import CrfModelMixin


class CareStatusBaseline(CrfModelMixin, edc_models.BaseUuidModel):

    hiv_result = models.CharField(
        verbose_name=mark_safe(
            "What was the result of the patient's most recent HIV test"
        ),
        max_length=15,
        choices=POS_NEG_NOTESTED,
        help_text="If positive, complete form `Hiv Initial Review`",
    )

    hiv_result_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient's most recent HIV test?",
        null=True,
        blank=True,
    )

    hiv_result_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="calculated by the EDC using `hiv_result_ago`",
    )

    hypertensive_tested = models.CharField(
        verbose_name="Has the patient ever tested for Hypertension?",
        max_length=15,
        choices=YES_NO,
    )

    hypertensive_tested_ago = edc_models.DurationYearMonthField(
        verbose_name="If Yes, how long ago was the patient tested for Hypertension?",
        null=True,
        blank=True,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe("Has the patient ever been diagnosed with Hypertension"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Hypertension Initial Review`",
    )

    hypertensive_tested_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        help_text="calculated by the EDC using `hypertensive_tested_ago`",
    )

    diabetic_tested = models.CharField(
        verbose_name="Has the patient ever tested for Diabetes?",
        max_length=15,
        choices=YES_NO,
    )

    diabetic_tested_ago = edc_models.DurationYearMonthField(
        verbose_name="If Yes, how long ago was the patient tested for Diabetes?",
        null=True,
        blank=True,
    )
    diabetic = models.CharField(
        verbose_name=mark_safe("Have you ever been diagnosed with Diabetes"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Diabetes Initial Review`",
    )

    diabetes_tested_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        help_text="calculated by the EDC using `diabetic_tested_ago`",
    )

    health_insurance = models.CharField(
        verbose_name="Does the patient have any private or work-place health insurance?",
        max_length=15,
        choices=YES_NO,
    )

    patient_club = models.CharField(
        verbose_name="Does the patient belong to a ‘club’ that supports medicines purchase?",
        max_length=15,
        choices=YES_NO,
    )

    def save(self, *args, **kwargs):
        if self.hiv_result_ago:
            self.hiv_result_estimated_datetime = edc_models.duration_to_date(
                self.hiv_result_ago, self.report_datetime
            )
        if self.diabetic_tested_ago:
            self.diabetes_tested_estimated_datetime = edc_models.duration_to_date(
                self.diabetic_tested_ago, self.report_datetime
            )
        if self.hypertensive_tested_ago:
            self.hypertensive_tested_estimated_datetime = edc_models.duration_to_date(
                self.hypertensive_tested_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Care Status: Baseline"
        verbose_name_plural = "Care Status: Baseline"
