from django.db import models
from edc_model.models import BaseUuidModel
from inte_lists.models import ArvRegimens

from ..crf_model_mixin import CrfModelMixin
from .treatment_model_mixin import TreatmentDetailModelMixin


class HivTreatmentLog(CrfModelMixin, BaseUuidModel):
    class Meta(CrfModelMixin.Meta):
        verbose_name = "HIV Treatment Log"
        verbose_name_plural = "HIV Treatment Log"


class HivTreatmentDetail(TreatmentDetailModelMixin, BaseUuidModel):

    treatment = models.ManyToManyField(ArvRegimens, verbose_name="Medicine",)

    class Meta:
        verbose_name = "HIV Treatment Log Detail"
        verbose_name_plural = "HIV Treatment Log Detail"
