from django.db import models
from edc_constants.choices import YES_NO
from edc_constants.constants import NO
from edc_model import models as edc_models

from inte_lists.models import ReasonsForTesting

from ..model_mixins import CrfModelMixin


class Investigations(CrfModelMixin, edc_models.BaseUuidModel):

    """Model not used"""

    hiv_tested = models.CharField(
        verbose_name="Was the patient tested for HIV infection?",
        max_length=15,
        choices=YES_NO,
        default=NO,
    )

    hypertension_tested = models.CharField(
        verbose_name="Was the patient tested for hypertension?",
        max_length=15,
        choices=YES_NO,
        default=NO,
    )

    diabetes_tested = models.CharField(
        verbose_name="Was the patient tested for diabetes?",
        max_length=15,
        choices=YES_NO,
        default=NO,
    )

    test_date = models.DateField(verbose_name="Date test requested", null=True, blank=True)

    reason = models.ManyToManyField(
        ReasonsForTesting, verbose_name="Why was the patient tested?", blank=True
    )

    reason_other = edc_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Investigations"
        verbose_name_plural = "Investigations"
