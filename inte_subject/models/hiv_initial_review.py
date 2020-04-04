from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_constants.choices import YES_NO
from edc_crf.model_mixins import CrfModelMixin
from edc_model.models import OtherCharField
from edc_model.models.base_uuid_model import BaseUuidModel
from edc_model.validators.date import date_not_future
from edc_reportable import CELLS_PER_MILLIMETER_CUBED_DISPLAY, COPIES_PER_MILLILITER
from inte_lists.models import ArvRegimens

from ..model_mixins import ReviewModelMixin


class HivInitialReview(ReviewModelMixin, CrfModelMixin, BaseUuidModel):
    diagnosis_date = models.DateField(
        verbose_name="When was the patient diagnosed with HIV?"
    )

    arv_initiation_date = models.DateField(
        verbose_name="Date of start of antiretroviral therapy (ART)",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    viral_load = models.IntegerField(
        verbose_name="Last viral load",
        validators=[MinValueValidator(0), MaxValueValidator(9999999)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    viral_load_date = models.DateField(
        verbose_name="Date of last viral load",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    cd4 = models.IntegerField(
        verbose_name="Last CD4",
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    )

    cd4_date = models.DateField(
        verbose_name="Date of last CD4",
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    current_arv_regimen = models.ForeignKey(
        ArvRegimens,
        on_delete=models.PROTECT,
        related_name="current_arv_regimen",
        verbose_name=(
            "Which antiretroviral therapy regimen is the patient currently on?"
        ),
        null=True,
        blank=False,
    )

    other_current_arv_regimen = OtherCharField(null=True, blank=True)

    class Meta(CrfModelMixin.Meta):
        verbose_name = "HIV Initial Review"
        verbose_name_plural = "HIV Initial Reviews"
