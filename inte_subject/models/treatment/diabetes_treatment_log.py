from django.db import models
from edc_model.models import BaseUuidModel
from inte_lists.models import DiabetesTreatment

from ..crf_model_mixin import CrfModelMixin
from .treatment_model_mixin import TreatmentDetailModelMixin


class DiabetesTreatmentLog(CrfModelMixin, BaseUuidModel):
    class Meta(CrfModelMixin.Meta):
        verbose_name = "Diabetes Treatment Log"
        verbose_name_plural = "Diabetes Treatment Log"


class DiabetesTreatmentDetail(TreatmentDetailModelMixin, BaseUuidModel):

    treatment = models.ManyToManyField(DiabetesTreatment, verbose_name="Medicine",)

    class Meta:
        verbose_name = "Diabetes Treatment Log Detail"
        verbose_name_plural = "Diabetes Treatment Log Detail"
