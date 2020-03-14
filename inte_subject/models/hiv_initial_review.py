from django.db import models
from edc_constants.constants import NOT_APPLICABLE
from edc_crf.model_mixins import CrfModelMixin
from edc_model import models as edc_models
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_model.validators.date import date_not_future
from inte_lists.models import ArvRegimens

from ..model_mixins import ReviewModelMixin


class HivInitialReview(ReviewModelMixin, CrfModelMixin, BaseUuidModel):
    diagnosis_date = models.DateField(
        verbose_name="When was the patient diagnosed with HIV?"
    )

    art_initiation_date = models.DateField(
        verbose_name="When was the patient initiated on ART?",
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text="Leave blank if not initiated",
    )

    art_initiation_date_estimated = edc_models.IsDateEstimatedFieldNa(
        verbose_name="Is the ART initiation date estimated", default=NOT_APPLICABLE,
    )

    treatment = models.ManyToManyField(
        ArvRegimens,
        verbose_name="If initiated on ART, which regimen is the patient currently receiving?",
    )

    last_viral_load = models.DecimalField(
        verbose_name="Most recent Viral Load, if known?",
        decimal_places=3,
        max_digits=10,
        null=True,
        blank=True,
        help_text="copies/mL",
    )

    viral_load_date = models.DateField(
        verbose_name="Viral Load collection date",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    vl_date_estimated = edc_models.IsDateEstimatedFieldNa(
        verbose_name="Is the subject's Viral Load collection date estimated?",
        default=NOT_APPLICABLE,
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "HIV Initial Review"
        verbose_name_plural = "HIV Initial Reviews"
