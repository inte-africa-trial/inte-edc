from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from inte_lists.models import ReasonsForTesting

from ..model_mixins import (
    ClinicalReviewModelMixin,
    CrfModelMixin,
    TreatmentPayMethodsModelMixin,
)


class ClinicalReview(
    TreatmentPayMethodsModelMixin,
    ClinicalReviewModelMixin,
    CrfModelMixin,
    edc_models.BaseUuidModel,
):

    hiv_test = models.CharField(
        verbose_name="Since last seen, was the patient tested for HIV infection?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=mark_safe(
            "Note: Select `not applicable` if diagnosis previously reported. <BR>"
            "`Since last seen` includes today.<BR>"
            "If `yes', complete the initial review CRF<BR>"
            "If `not applicable`, complete the review CRF."
        ),
    )

    hiv_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    hiv_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="hiv_test_reason",
        verbose_name="Why was the patient tested for HIV infection?",
        blank=True,
    )

    hiv_reason_other = edc_models.OtherCharField()

    hiv_dx = models.CharField(
        verbose_name=mark_safe(
            "As of today, was the patient <u>newly</u> diagnosed with HIV infection?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    htn_test = models.CharField(
        verbose_name="Since last seen, was the patient tested for hypertension?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=mark_safe(
            "Note: Select `not applicable` if diagnosis previously reported. <BR>"
            "`Since last seen` includes today.<BR>"
            "If `yes', complete the initial review CRF<BR>"
            "If `not applicable`, complete the review CRF."
        ),
    )

    htn_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    htn_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="htn_test_reason",
        verbose_name="Why was the patient tested for hypertension?",
        blank=True,
    )

    htn_reason_other = edc_models.OtherCharField()

    htn_dx = models.CharField(
        verbose_name=mark_safe(
            "As of today, was the patient <u>newly</u> diagnosed with hypertension?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    dm_test = models.CharField(
        verbose_name="Since last seen, was the patient tested for diabetes?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=mark_safe(
            "Note: Select `not applicable` if diagnosis previously reported. <BR>"
            "`Since last seen` includes today.<BR>"
            "If `yes', complete the initial review CRF<BR>"
            "If `not applicable`, complete the review CRF."
        ),
    )

    dm_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    dm_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="dm_reason",
        verbose_name="Why was the patient tested for diabetes?",
        blank=True,
    )

    dm_reason_other = edc_models.OtherCharField()

    dm_dx = models.CharField(
        verbose_name=mark_safe(
            "As of today, was the patient <u>newly</u> diagnosed with diabetes?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    complications = models.CharField(
        verbose_name="Since last seen, has the patient had any complications",
        max_length=15,
        choices=YES_NO,
        help_text="If Yes, complete the `Complications` CRF",
    )
    # QUESTION_RETIRED
    test_date = models.DateField(
        verbose_name="Date test requested",
        null=True,
        blank=True,
        editable=False,
        help_text="question_retired",
    )

    # QUESTION_RETIRED
    reason = models.ManyToManyField(
        ReasonsForTesting,
        verbose_name="Why was the patient tested?",
        blank=True,
        editable=False,
        help_text="question_retired",
    )

    reason_other = edc_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Clinical Review"
        verbose_name_plural = "Clinical Reviews"
