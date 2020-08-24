from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import POS_NEG_NOTESTED, YES_NO, YES_NO_NA
from edc_constants.constants import NO, NOT_APPLICABLE, POS, YES
from edc_model import models as edc_models
from edc_model.models import date_not_future


class ClinicalReviewHivModelMixin(models.Model):

    hiv_tested = models.CharField(
        verbose_name=mark_safe(
            "What was the result of the patient's most recent HIV test"
        ),
        max_length=15,
        choices=POS_NEG_NOTESTED,
        help_text="If positive, complete form `Hiv Initial Review`",
    )

    hiv_tested_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient's most recent HIV test?",
        null=True,
        blank=True,
        help_text="If positive, most recent HIV(+) test",
    )

    hiv_tested_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text="calculated by the EDC using `hiv_tested_ago`",
    )

    hiv_tested_date = models.DateField(
        validators=[date_not_future], null=True, blank=True
    )

    hiv_dx = models.CharField(
        verbose_name=mark_safe("Was the patient diagnosed with HIV infection?"),
        max_length=15,
        choices=YES_NO,
        null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        # TODO: update hiv_dx on existing data
        if self.hiv_tested == POS:
            self.hiv_dx = YES
        else:
            self.hiv_dx = NO
        if self.hiv_tested_ago:
            self.hiv_tested_estimated_datetime = edc_models.duration_to_date(
                self.hiv_tested_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ClinicalReviewHypertensionModelMixin(models.Model):

    hypertension_tested = models.CharField(
        verbose_name="Has the patient ever tested for Hypertension?",
        max_length=15,
        choices=YES_NO,
    )

    hypertension_tested_ago = edc_models.DurationYearMonthField(
        verbose_name="If Yes, how long ago was the patient tested for Hypertension?",
        null=True,
        blank=True,
    )

    hypertension_tested_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        help_text="calculated by the EDC using `hypertension_tested_ago`",
    )

    hypertension_tested_date = models.DateField(
        validators=[date_not_future], null=True, blank=True
    )

    hypertension_dx = models.CharField(
        verbose_name=mark_safe("Has the patient ever been diagnosed with Hypertension"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Hypertension Initial Review`",
    )

    def save(self, *args, **kwargs):
        if self.hypertension_tested_ago:
            self.hypertension_tested_estimated_datetime = edc_models.duration_to_date(
                self.hypertension_tested_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class ClinicalReviewDiabetesModelMixin(models.Model):

    diabetes_tested = models.CharField(
        verbose_name="Has the patient ever tested for Diabetes?",
        max_length=15,
        choices=YES_NO,
    )

    diabetes_tested_ago = edc_models.DurationYearMonthField(
        verbose_name="If Yes, how long ago was the patient tested for Diabetes?",
        null=True,
        blank=True,
    )

    diabetes_tested_estimated_datetime = models.DateTimeField(
        null=True,
        blank=True,
        help_text="calculated by the EDC using `diabetes_tested_ago`",
    )

    diabetes_tested_date = models.DateField(
        validators=[date_not_future], null=True, blank=True
    )

    diabetes_dx = models.CharField(
        verbose_name=mark_safe("Have you ever been diagnosed with Diabetes"),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="If yes, complete form `Diabetes Initial Review`",
    )

    def save(self, *args, **kwargs):
        if self.diabetes_tested_ago:
            self.diabetes_tested_estimated_datetime = edc_models.duration_to_date(
                self.diabetes_tested_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
