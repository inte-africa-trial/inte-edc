from django.db import models
from edc_constants.choices import YES_NO
from edc_model.models import BaseUuidModel
from inte_lists.models import Conditions

from ..crf_model_mixin import CrfModelMixin


class GeneralAssessment(CrfModelMixin, BaseUuidModel):
    conditions = models.ManyToManyField(
        Conditions, verbose_name="On what basis was the patient enrolled?",
    )

    hiv_screen = models.CharField(
        verbose_name="Besides the tests done today, have you been tested for HIV?",
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="HIV",
    )

    hiv_informed = models.CharField(
        verbose_name="Were you told you are HIV positive?",
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="HIV",
    )

    hiv_screen_date = models.DateField(
        verbose_name="How long ago was this",
        null=True,
        blank=True,
        help_text="HIV. If estimated, see protocol for instructions on how to estimate dates",
    )

    diabetes_screen = models.CharField(
        verbose_name=(
            "Besides the tests done today, have you been tested "
            "for diabetes (high blood sugar)"
        ),
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="Diabetes",
    )

    diabetes_informed = models.CharField(
        verbose_name="Were you told you have diabetes?",
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="Diabetes",
    )

    diabetes_screen_date = models.DateField(
        verbose_name="How long ago was this?",
        null=True,
        blank=True,
        help_text=(
            "Diabetes. If estimated, see protocol for instructions on how to estimate dates"
        ),
    )

    hypertension_screen = models.CharField(
        verbose_name=(
            "Besides the tests done today, have you been "
            "tested for high blood pressure?"
        ),
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="Hypertension",
    )

    hypertension_informed = models.CharField(
        verbose_name="Were you told you have high blood pressure?",
        choices=YES_NO,
        max_length=15,
        null=True,
        blank=True,
        help_text="Hypertension",
    )

    hypertension_screen_date = models.DateField(
        verbose_name="How long ago was this?",
        null=True,
        blank=True,
        help_text=(
            "Hypertension. If estimated, see protocol for instructions "
            "on how to estimate dates"
        ),
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "General Assessment"
        verbose_name_plural = "General Assessment"
