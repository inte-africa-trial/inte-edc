from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE, NOT_ESTIMATED, YES
from edc_model import models as edc_models
from inte_subject.diagnoses import Diagnoses


class InitialReviewModelError(Exception):
    pass


class InitialReviewModelMixin(models.Model):

    dx_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago was the patient diagnosed?",
        null=True,
        blank=True,
        help_text="If possible, provide the exact date below instead of estimating here.",
    )

    dx_date = models.DateField(
        verbose_name="Date patient diagnosed",
        null=True,
        blank=True,
        help_text="If possible, provide the exact date here instead of estimating above.",
    )

    dx_estimated_date = models.DateField(
        verbose_name="Estimated diagnoses date",
        null=True,
        editable=False,
        help_text="Calculated based on response to `dx_ago`",
    )

    dx_date_estimated = models.CharField(
        verbose_name="Was the diagnosis date estimated?",
        max_length=15,
        choices=YES_NO,
        default=YES,
        editable=False,
    )

    def save(self, *args, **kwargs):
        diagnoses = Diagnoses(
            subject_identifier=self.subject_visit.subject_identifier,
            report_datetime=self.subject_visit.report_datetime,
            lte=True,
        )
        if not diagnoses.get_dx_by_model(self) == YES:
            raise InitialReviewModelError(
                "No diagnosis has been recorded. See clinical review. "
                "Perhaps catch this in the form."
            )
        super().save(*args, **kwargs)

    def get_best_dx_date(self):
        return self.dx_date or self.dx_estimated_date

    class Meta:
        abstract = True


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

    def save(self, *args, **kwargs):
        if not self.dx_ago and not self.dx_date:
            raise InitialReviewModelError(
                "Expected either `dx_ago` or `dx_date`. "
                f"Perhaps catch this in the form. See {self}."
            )
        if self.dx_ago:
            self.dx_estimated_date = edc_models.duration_to_date(
                self.dx_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
