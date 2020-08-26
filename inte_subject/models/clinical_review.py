from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from inte_lists.models import ReasonsForTesting

from ..model_mixins import CrfModelMixin


class ClinicalReview(CrfModelMixin, edc_models.BaseUuidModel):

    hiv_tested = models.CharField(
        verbose_name="Since last seen, was the patient tested for HIV infection?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=(
            "Select `not applicable` if previously diagnosed. "
            "`Since last seen` includes today."
        ),
    )

    hiv_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    hiv_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="hiv_tested_reason",
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

    hypertension_tested = models.CharField(
        verbose_name="Since last seen, was the patient tested for hypertension?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=(
            "Select `not applicable` if previously "
            "diagnosed. `Since last seen` includes today."
        ),
    )

    hypertension_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    hypertension_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="hypertension_tested_reason",
        verbose_name="Why was the patient tested for hypertension?",
        blank=True,
    )

    hypertension_reason_other = edc_models.OtherCharField()

    hypertension_dx = models.CharField(
        verbose_name=mark_safe(
            "As of today, was the patient <u>newly</u> diagnosed with hypertension?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    diabetes_tested = models.CharField(
        verbose_name="Since last seen, was the patient tested for diabetes?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=(
            "Select `not applicable` if previously diagnosed. "
            "`Since last seen` includes today."
        ),
    )

    diabetes_test_date = models.DateField(
        verbose_name="Date test requested", null=True, blank=True,
    )

    diabetes_reason = models.ManyToManyField(
        ReasonsForTesting,
        related_name="diabetes_tested_reason",
        verbose_name="Why was the patient tested for diabetes?",
        blank=True,
    )

    diabetes_reason_other = edc_models.OtherCharField()

    diabetes_dx = models.CharField(
        verbose_name=mark_safe(
            "As of today, was the patient <u>newly</u> diagnosed with diabetes?"
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
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
