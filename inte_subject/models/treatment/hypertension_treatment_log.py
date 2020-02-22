from django.db import models
from edc_model.models import BaseUuidModel
from inte_lists.models import HypertensionTreatment

from ..crf_model_mixin import CrfModelMixin
from .treatment_model_mixin import TreatmentDetailModelMixin


class HypertensionTreatmentLog(CrfModelMixin, BaseUuidModel):
    class Meta(CrfModelMixin.Meta):
        verbose_name = "Hypertension Treatment Log"
        verbose_name_plural = "Hypertension Treatment Log"


class HypertensionTreatmentDetail(TreatmentDetailModelMixin, BaseUuidModel):

    treatment = models.ManyToManyField(HypertensionTreatment, verbose_name="Medicine",)

    class Meta:
        verbose_name = "Hypertension Treatment Log Detail"
        verbose_name_plural = "Hypertension Treatment Log Detail"
