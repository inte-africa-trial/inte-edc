from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_PENDING_NA, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, YES
from edc_lab.choices import VL_QUANTIFIER_NA
from edc_model import models as edc_models
from edc_reportable import CELLS_PER_MILLIMETER_CUBED_DISPLAY, COPIES_PER_MILLILITER

from ..choices import CARE_ACCESS
from ..model_mixins import CrfModelMixin, InitialReviewModelMixin


class HivInitialReview(
    InitialReviewModelMixin, CrfModelMixin, edc_models.BaseUuidModel
):

    receives_care = models.CharField(
        verbose_name="Is the patient receiving care for HIV",
        max_length=15,
        choices=YES_NO,
    )

    clinic = models.CharField(
        verbose_name="Where does the patient receive care for HIV",
        max_length=15,
        choices=CARE_ACCESS,
        default=NOT_APPLICABLE,
    )

    clinic_other = models.CharField(
        verbose_name=mark_safe(
            "If <u>not</u> attending here, where does the patient attend?"
        ),
        max_length=50,
        null=True,
        blank=True,
    )

    arv_initiation_ago = edc_models.DurationYearMonthField(
        verbose_name="How long ago did the patient start ART?", null=True, blank=True,
    )

    arv_initiation_estimated_date = models.DateField(
        verbose_name="Date of start of antiretroviral therapy (ART)",
        validators=[edc_models.date_not_future],
        null=True,
        editable=False,
        help_text="Calculated based on response to `arv_initiation_ago`",
    )

    arv_initiation_date_estimated = models.CharField(
        verbose_name="Was the date patient started ART estimated?",
        max_length=15,
        choices=YES_NO,
        default=YES,
        editable=False,
    )

    # Viral Load
    has_vl = models.CharField(
        verbose_name="Is the patient's most recent viral load result available?",
        max_length=25,
        choices=YES_NO_PENDING_NA,
        default=NOT_APPLICABLE,
    )
    vl = models.IntegerField(
        verbose_name="Most recent viral load",
        validators=[MinValueValidator(0), MaxValueValidator(9999999)],
        null=True,
        blank=True,
        help_text=COPIES_PER_MILLILITER,
    )

    vl_quantifier = models.CharField(
        max_length=10, choices=VL_QUANTIFIER_NA, null=True, blank=True,
    )

    vl_date = models.DateField(
        verbose_name="Date of most recent viral load",
        validators=[edc_models.date_not_future],
        null=True,
        blank=True,
    )

    # CD4
    has_cd4 = models.CharField(
        verbose_name="Is the patient's most recent CD4 result available?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    cd4 = models.IntegerField(
        verbose_name="Most recent CD4",
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text=CELLS_PER_MILLIMETER_CUBED_DISPLAY,
    )

    cd4_date = models.DateField(
        verbose_name="Date of most recent CD4",
        validators=[edc_models.date_not_future],
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.dx_ago:
            self.dx_estimated_date = edc_models.duration_to_date(
                self.dx_ago, self.report_datetime
            )
        if self.arv_initiation_ago:
            self.arv_initiation_estimated_date = edc_models.duration_to_date(
                self.arv_initiation_ago, self.report_datetime
            )
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "HIV Initial Review"
        verbose_name_plural = "HIV Initial Reviews"
