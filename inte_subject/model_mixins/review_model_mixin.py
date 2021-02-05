from django.db import models
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, YES
from edc_model import models as edc_models

from inte_subject.diagnoses import Diagnoses


class InitialReviewModelError(Exception):
    pass


class InitialReviewModelMixin(models.Model):

    dx_ago = edc_models.DurationYMDField(
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
        help_text="Calculated based on response to `dx_ago`",
        editable=False,
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

    care_delivery = models.CharField(
        verbose_name=(
            "Was care for this `condition` delivered " "in an integrated care clinic today?"
        ),
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text="Select `not applicable` if site was not selected for integrated care.",
    )

    care_delivery_other = models.TextField(
        verbose_name="If no, please explain", null=True, blank=True
    )

    class Meta:
        abstract = True
