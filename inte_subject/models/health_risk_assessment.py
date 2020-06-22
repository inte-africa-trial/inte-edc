from django.db import models
from edc_constants.choices import YES_NO, SMOKER_STATUS_SIMPLE
from edc_constants.constants import NOT_APPLICABLE, SMOKER
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models

from ..choices import ALCOHOL_CONSUMPTION


class HealthRiskAssessment(CrfModelMixin, edc_models.BaseUuidModel):
    smoking_status = models.CharField(
        verbose_name="Which of these options describes you",
        max_length=15,
        choices=SMOKER_STATUS_SIMPLE,
    )

    smoker_quit_ago = edc_models.DurationYearMonthField(
        verbose_name="If you used to smoke but stopped, how long ago did you stop",
        null=True,
        blank=True,
    )

    smoker_quit_estimated_date = models.DateField(
        verbose_name="Estimated date smoker quit?", null=True, editable=False,
    )

    alcohol = models.CharField(
        verbose_name="Do you drink alcohol?", max_length=15, choices=YES_NO,
    )

    alcohol_consumption = models.CharField(
        verbose_name="If yes, how often do you drink alcohol?",
        max_length=25,
        choices=ALCOHOL_CONSUMPTION,
        default=NOT_APPLICABLE,
    )

    def save(self, *args, **kwargs):
        if self.smoker_quit_ago:
            self.smoker_quit_estimated_date = edc_models.duration_to_date(
                self.smoker_quit_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Health Risk Assessment"
        verbose_name_plural = "Health Risk Assessments"
