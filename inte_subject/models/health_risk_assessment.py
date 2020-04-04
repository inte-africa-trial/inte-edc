from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models import BaseUuidModel
from edc_model.validators import ym_validator

from ..choices import ALCOHOL_CONSUMPTION, SMOKER_STATUS


class HealthRiskAssessment(CrfModelMixin, BaseUuidModel):
    smoking_status = models.CharField(
        verbose_name="Which of these options describes you",
        max_length=15,
        choices=SMOKER_STATUS,
    )

    smoker_quit_ago_str = models.CharField(
        verbose_name="If you used to smoke but stopped, how long ago did you stop",
        max_length=8,
        validators=[ym_validator],
        null=True,
        blank=True,
        help_text=(
            "Duration since last smoked. Format is `YYyMMm`. For example 1y11m, 12y7m, etc"
        ),
    )

    smoker_quit_ago_months = models.IntegerField(editable=False, null=True)

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
        # TODO: calculate smoker quit months
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "Health Risk Assessment"
        verbose_name_plural = "Health Risk Assessments"
